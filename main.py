from internet import *
from api_calls import *
from logic import *



# test playlist id = 60QjB7v7V8If58q661ZzOj
# echte drip drop playlist id = 6NYUUALff1pcZRJHaLpvRA
# drip drop backup playlist id = 7kEpthO12IIpyOSuXnxPXD

"""
Reihenfolge:
1. Playlists vergleichen
2. Fehlende Songs zu backup Playlist adden
3. song_dict mit dripdrop Playlist erstellen
4. song_dict runterkürzen auf Songs die älter als 91 Tage sind
5. favorite tag dem song_dict hinzufügen
6. song_dict kürzen, sodass nur unfavorites drin sind
7. Songs aus dripdrop removen
"""

def main():

    # 0. Initialisierung der Klassen
    i = Internet()
    a = ApiCalls(i.give_valid_access_token())
    l = Logic()

    # 1. Playlists vergleichen
    songs_to_add = l.playlist_comparison(realplaylist="6NYUUALff1pcZRJHaLpvRA", backupplaylist="7kEpthO12IIpyOSuXnxPXD")

    # 2. Fehlende Songs zu backup Playlist adden
    a.add_tracks(songs_to_add)

    # 3. song_dict mit dripdrop Playlist erstellen
    song_dict = a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA")

    # 4. song_dict runterkürzen auf Songs die älter als 91 Tage sind
    song_dict = l.time_dict_shortener(song_dict)

    # 5. favorite tag dem song_dict hinzufügen
    l.favorite_dict_adder(song_dict)

    # 6. song_dict kürzen, sodass nur unfavorites drin sind
    song_dict = l.unfavorite_shortener(song_dict)

    # 7. Songs aus dripdrop entfernen
    a.remove_songs_from_playlist(song_dict)
