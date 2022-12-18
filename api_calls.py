import math
from internet import *


class ApiCalls:
    
    access_token = ""
    playlist_id = ""
    i = Internet()


    def __init__(self, access_token):
        self.access_token = access_token
        # test playlist id = 60QjB7v7V8If58q661ZzOj
        # echte drip drop playlist id = 6NYUUALff1pcZRJHaLpvRA 
        self.playlist_id = "60QjB7v7V8If58q661ZzOj"

    
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
    def get_playlist_items(self, playlist_id):
        url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        params = {
            "limit": 50,
            "fields": "total, next, items(track(name, uri), added_at)"
        }

        r = requests.get(url=url, headers=headers, params=params)
        playlist_obj = r.json()
        

        # Liste mit allen Songs der Playlist erstellen
        song_list = []
        needed_request_amount = math.ceil(playlist_obj["total"] / 50)
        # äußere Schleife macht requests und erhält 50er liste an songs,
        # die dann zu neuem einfacherem dict processed werden und in song_list geaddet werden
        # nach jedem Durchlauf, wird current_part_playlist_obj auf den nächsten Teilabschnitt aktualisiert
        # counter = 1
        current_part_playlist_obj = playlist_obj
        for i in range(0, needed_request_amount):
            current_items = current_part_playlist_obj["items"]
            for song in current_items:
                song_dict = {
                    "name": song["track"]["name"],
                    "added_at": song["added_at"],
                    "uri": song["track"]["uri"]
                }
                song_list.append(song_dict)
                # print(str(counter) + ". " + song_dict["name"] + " hinzugeüft am: " + song_dict["added_at"])
                # counter += 1
            
            # nur wenn es nicht die letzte request ist, wird das current_part_playlist_obj geupdatet
            if i != needed_request_amount-1:
                next_url = current_part_playlist_obj["next"]
                current_part_playlist_obj = self.basic_api_call(next_url)    

        # Liste nach Datum sortieren
        song_list.sort(key=lambda item:item["added_at"])

        return song_list

    
    # Song Removal Funktion
    # Nimmt als argument eine Liste von song dicts
    def remove_songs_from_playlist(self, songs_to_remove):
        url = "https://api.spotify.com/v1/playlists/" + self.playlist_id + "/tracks"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        json_song_dicts = json.dumps(songs_to_remove)
        data = '{"tracks": ' + json_song_dicts + '}'
        r = requests.delete(url=url, headers=headers, data=data)
        return r.content


    # Test Funktion um Favorite Check auszuprobieren,
    # später durch track argument verallgemeinern
    def is_track_favorite(self, songs_to_check):
        # liste mit song dicts zu String mit song ids durch Kommas getrennt converten
        songs_string = ""
        for song_dict in songs_to_check:
            song_id = song_dict["uri"][14:]
            songs_string += song_id + ","

        # eigentlicher Request
        url = "https://api.spotify.com/v1/me/tracks/contains"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        params = {
            "ids" : songs_string
        }
        r = requests.get(url=url, headers=headers, params=params)
        return r.json()