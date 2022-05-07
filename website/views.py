from django.shortcuts import render
from musicapy.saavn_api.api import SaavnAPI

api = SaavnAPI()


def index(request):
    context = {"title": "HomePage", "search_for": "Song/Album Name/Saavn Link",
               "active_page": "home", "search_method": "search_all"}

    if request.method == 'POST':
        query = request.POST.get('search_all', None)
        if query:
            data = api.search_all(str(query))
            context["search_result"] = data

    return render(request, 'index.html', context=context)


def songs_page(request):
    context = {"title": "Songs", "search_for": "Song Name/Saavn Link",
               "active_page": "songs", "search_method": "search_songs"}
    if request.method == 'POST':
        song_query = request.POST.get('search_songs', None)
        if song_query:
            data = api.search_song(song_query)
            context['search_result'] = data

    return render(request, 'songs.html', context=context)


def albums_page(request):
    context = {"title": "Albums", "search_for": "Album Name/Saavn Link",
               "active_page": "albums", "search_method": "search_albums"}
    if request.method == 'POST':
        album_query = request.POST.get('search_albums', None)
        if album_query:
            data = api.search_album(album_query)
            context['search_result'] = data

    return render(request, 'albums.html', context=context)
