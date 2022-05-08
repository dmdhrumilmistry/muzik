from django.shortcuts import render
from musicapy.saavn_api.api import SaavnAPI

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


def download_songs(request):
    def dict_to_list(dictionary): return [[k, v]
                                          for k, v in dictionary.items()]

    context = {"title": "Download Page", "search_for": "Song/Album Name/Saavn Link"}
    req_type = 'invalid'
    songs_payload = []
    if request.method == 'GET':
        link = request.GET.get('link', False)
        context['link'] = link
        if link and 'song' in link and 'saavn' in link:
            req_type = 'song'
            identifier = api.create_identifier(link, 'song')
            download_links = api.get_download_links(identifier)

            song_details = api.get_song_details(identifier, use_v4=True)
            song_details = song_details.get('songs', [False])[0]

            songs_payload = [{
                'song': song_details.get('title'),
                'image': song_details.get('image'),
                'links': dict_to_list(download_links)
            }]

        elif link and 'album' in link and 'saavn' in link:
            req_type = 'album'
            identifier = api.create_identifier(link, 'album')
            songs_payload = api.generate_album_download_links(identifier)
            if songs_payload:
                songs_payload = songs_payload.get('songs')

            for song_payload in songs_payload:
                song_payload['links'] = dict_to_list(
                    song_payload.get('links', {'msg': 'not fount'}))

        else:
            context['type'] = 'invalid'
            download_links = None

        context['payload'] = {'type': req_type, 'songs': songs_payload}
    return render(request, 'download.html', context=context)
