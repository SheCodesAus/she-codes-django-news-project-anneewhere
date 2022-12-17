from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountPageView(generic.DetailView):
    model = CustomUser
    template_name = 'users/accountpage.html'
    context_object_name: 'CustomUser'

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    ssuccess_url = reverse_lazy('users:accountpage')
    template_name = 'users/editAccount.html'

    def get_success_url(self):
        print(self.request.user.id)
        print(type(self.get_form()))
        return reverse_lazy('users:profile', kwargs={"pk":self.request.user.id})
        
    def get_object(self):
        return self.request.user