from django.shortcuts import render
from musicapy.saavn_api.api import SaavnAPI
from pprint import pprint

api = SaavnAPI()


def index(request):
    context = {"title": "HomePage", "search_for": "Song/Album Name/Saavn Link",
               "active_page": "home", "search_method": "search_all"}

    if request.method == 'POST':
        query = request.POST.get('search_all', None)

        data = None
        if query and 'saavn' in query:
            if 'song' in query:
                identifier = api.create_identifier(query, 'song')
                data = api.get_song_details(identifier)

                pprint(data)
                songs = []
                for song in data.get('songs', []):
                    song_data = {"title": song.get('song', None), "image": song.get('image', None), "year": song.get(
                        'year', None), "subtitle": song.get('primary_artists', None), "perma_url": song.get('perma_url', None), "type": "song"}
                    songs.append(song_data)
                data = {"results": songs}

            elif 'album' in query:
                identifier = api.create_identifier(query, 'album')
                data = api.get_album_details(identifier)

                # format album
                data = {"results": [{"title": data.get('title', None), "image": data.get(
                    'image', None), "year": data.get('year', None), "subtitle": data.get('primary_artists', None), "perma_url": data.get('perma_url', None), "type": "album"}]}
        elif query:
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
    # elif request.method == 'GET':
        # data = api.get_trending()
        # context['search_result'] = {'results' : data}

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
