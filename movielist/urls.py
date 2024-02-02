from django.urls import path
from . import views
from .views import get_movie_name


urlpatterns = [
    
   path('hello/',views.hello),
   path('get_movie_name/',get_movie_name,name='url'),
]