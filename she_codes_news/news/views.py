from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Category
from .forms import StoryForm
from django.contrib.auth import get_user_model

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date') #new addtion from orderby
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
# the only logic applied to this within the html is just defining how the title and content has been displayed

class AuthorProfileView(generic.DetailView):
    model = get_user_model()
    template_name = 'news/profileDetail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author='author')
        return context

class CategoryView(generic.ListView):
        template_name = 'news/categoryView.html'
        model = NewsStory, Category

        def get_queryset(self):
            '''Return all news stories in chosen category.'''
            return NewsStory.objects.all(Category)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categorised_stories'] = NewsStory.objects.all(Category).order_by('-pub_date')[:4]
            return context

class EditStoryView(generic.edit.UpdateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    model = NewsStory
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:story')

    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:profile', kwargs={"pk":self.request.user.id})
        
    def get_object(self):
        return self.request.user

class deleteStoryView(generic.edit.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

    def get_object(self):
        return self.request.user