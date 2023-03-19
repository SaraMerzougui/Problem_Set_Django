
from django.urls import path
from .views import homepage , addjoke,joke
urlpatterns = [
    path('',homepage , name='homepage'),
    path('add/', addjoke,name='addjoke'),
    path('joke/<int:id>', joke, name='joke'),
]
