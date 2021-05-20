from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.home, name='home'),
    path("new_tweet/", views.create_tweet, name='create_tweet')
]