from .views import *
from django.urls import path

urlpatterns = [

    path('', index, name='index'),
    path('<slug:movie_slug>/', show_one_movie, name='show_one_movie')
]