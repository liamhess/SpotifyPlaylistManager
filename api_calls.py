from internet import *


class ApiCalls:
    
    access_token = ""
    playlist_id = ""


    def __init__(self, access_token):
        self.access_token = access_token
        # test playlist id = 60QjB7v7V8If58q661ZzOj
        self.playlist_id = "6NYUUALff1pcZRJHaLpvRA"

    
    # Get Current User's Playlists Api Call
    # Alle eigenen und gespeicherten Playlists sehen
    # gibt Liste mit allen Playlists aus
    def users_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }

        r = requests.get(url=url, headers=headers)
        return r.json()["items"]


    # Basic Api Call mit URL als Parameter und den zwei Authorization und Content-Type headern
    def basic_api_call(self, url):
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        r = requests.get(url=url, headers=headers)
        return r.json()


    # Get Playlist Api Call
    # gibt Liste aller Songs der Playlist nach Datum sortiert aus
    def get_playlist_items(self):
        url = "https://api.spotify.com/v1/playlists/" + self.playlist_id + "/tracks"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        params = {
            "limit": 1,
            "fields": "items(track(name), added_at)"
        }

        r = requests.get(url=url, headers=headers, params=params)
        playlist_obj = r.json()
        return playlist_obj

# WARUM IST DIE ITEMS LIST IN DER RESPONES LEER????