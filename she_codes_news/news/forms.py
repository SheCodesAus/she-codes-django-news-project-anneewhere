from django import forms
from django.forms import ModelForm
from .models import NewsStory, Category

choices = Category.objects.all().values_list

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'newsCategory', 'content', 'image_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
            'newsCategory': forms.Select(attrs={'class':'form-control'})
}

