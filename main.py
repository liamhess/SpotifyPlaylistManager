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


def testmain():
    print("Hello World")
    i = Internet()
    a = ApiCalls(i.give_valid_access_token())
    l = Logic()
    a.remove_songs_from_playlist()
    


def main():

    # 0. Initialisierung der Klassen
    i = Internet()
    a = ApiCalls(i.give_valid_access_token())
    l = Logic()
    
    print("Access Token valid: " + str(i.access_token_check()))
    
    # 1. Playlists vergleichen
    print("comparing playlists...")
    songs_to_add = l.playlist_comparison(realplaylist=a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA"), backupplaylist=a.get_playlist_items("7kEpthO12IIpyOSuXnxPXD"))
    print("comparing playlists done")

    # 2. Fehlende Songs zu backup Playlist adden
    print("adding tracks to backup...")
    a.add_tracks(songs_to_add, "7kEpthO12IIpyOSuXnxPXD")
    print("adding tracks to backup done")

    # 3. song_dict mit dripdrop Playlist erstellen
    print("creating song_dict...")
    song_dict = a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA")
    print("creating song_dict done")

    # 4. song_dict runterkürzen auf Songs die älter als 91 Tage sind
    print("time shortening song_dict...")
    song_dict = l.time_dict_shortener(song_dict)
    print("time shortening song_dict done")

    # 5. favorite tag dem song_dict hinzufügen
    print("adding favorite tag...")
    l.favorite_dict_adder(song_dict)
    print("adding favorite tag done")

    # 6. song_dict kürzen, sodass nur unfavorites drin sind
    print("favorite shortening song_dict...")
    song_dict = l.unfavorite_shortener(song_dict)
    print("favorite shortening song_dict done")

    # 7. Songs aus dripdrop entfernen
    print("removing songs...")
    a.remove_songs_from_playlist(song_dict, "6NYUUALff1pcZRJHaLpvRA")
    print("removing songs done")
