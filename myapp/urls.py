from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path('new_search', views.newSearch, name='newSearch'),
    path('', views.homeView, name = 'home')
]