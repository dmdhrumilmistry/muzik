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
            print(data)
            context["search_result"] = data

        
    return render(request, 'index.html', context=context)


def songs_page(request):
    return render(request, 'songs.html', context={"title": "Songs", "search_for": "Song Name/Saavn Link", "active_page": "songs", "search_method": "search_songs"})


def albums_page(request):
    return render(request, 'albums.html', context={"title": "Albums", "search_for": "Album Name/Saavn Link", "active_page": "albums", "search_method": "search_albums"})
