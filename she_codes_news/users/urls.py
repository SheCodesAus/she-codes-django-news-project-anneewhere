from django.urls import path
from .views import CreateAccountView, AccountPageView, EditAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),name='createAccount'),
    path('<int:pk>/', AccountPageView.as_view(), name='accountpage'),
    path('edit-account/', EditAccountView.as_view(), name='editAccount'),
]