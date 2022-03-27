CLIENT_ID = '1dd6eccf472241779ec81d2d76a727ef'
CLIENT_SECRET = '5ed23a047e1c4ccf91197e55f1345d72'
AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'

#artist name, album name, song name
import requests
import json

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

def get_song_info(song_id):
    track_request = requests.get(BASE_URL + 'tracks/' + song_id, headers=headers)
    track_request_json = track_request.json()

    artist_name = track_request_json.get("artists")[0].get('name')
    album_name = track_request_json.get("album").get('name')
    track_name = track_request_json.get('name')

    songInfoList = [artist_name, album_name, track_name]

    return songInfoList

    # print("artist name - " + artist_name)
    # print("album name - " + album_name)
    # print("track name - " + track_name)


def get_playlist(playlist_id):
    playlist_request = requests.get(BASE_URL + 'playlists/' + playlist_id, headers=headers)
    playlist_request_json = playlist_request.json()
    playlist = playlist_request_json.get("tracks").get('items')
    playlist_len = len(playlist)

    artist_album = {}

    for count in range(playlist_len):
        tracks = playlist[count].get('track').get('id')
        songInfoList = get_song_info(tracks)
        artist_name = songInfoList[0]
        album_name = songInfoList[1]
        track_name = songInfoList[2]
        album_song = {}
        album_song[album_name] = track_name
        artist_album[artist_name] = album_name
        for x in artist_album.values():
            if album_name == x:
                artist_album[artist_name] = album_song
        if count > 4:
            break

    return artist_album

#print(get_playlist('3r4wfURTAooB0Hapr6epub'))
#get_song_info('2374M0fQpWi3dLnB54qaLX')
#get_playlist('1DBuRmX1AdiIIFjWSwppRQ')
#get_song_info('2fpKkOzGcJ1tnBDnu8kJmp')