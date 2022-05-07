from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.albums_page, name='songs_page'),
    path('songs', views.songs_page, name='albums_page'),
]
