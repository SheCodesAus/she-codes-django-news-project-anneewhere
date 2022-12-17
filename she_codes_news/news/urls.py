from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # each url brings us to a specific page. this brings us to index. so when we create a url pattern, it will already start from news/ because it was defined in the main folder
    # views.IndexView = views(refers views.py and the specific class within that page)
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # sending us to specific primary key (the page). by default, django gives a story each unique identifier
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('<int:pk>', views.AuthorProfileView.as_view(), name="profileDetail")
]
