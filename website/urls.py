from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.albums_page, name='songs_page'),
    path('songs', views.songs_page, name='albums_page'),
    path('download', views.download_songs, name='download_songs'),
]
