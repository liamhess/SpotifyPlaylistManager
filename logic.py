from datetime import datetime, timedelta
from api_calls import *
from internet import *


class Logic:

    i = Internet()
    a = ApiCalls(i.give_valid_access_token())


    # Fügt zum songdict den key "favorite" hinzu, um später leichter checken zu können, welche Songs entfernt werden
    # und welchen nicht
    def favorite_dict_adder(self, songdict):
        favorite_list = self.a.is_track_favorite(songdict)
        
        for i in range(0, len(songdict)):
            songdict[i]["favorite"] = favorite_list[i]
        
        return songdict

    
    # Funktion, die im songdict die Zeitgrenze findet und es dann runterkürzt, auf die songs die im Entfern-Zeitraum liegen
    def time_dict_shortener(self, songdict):
        breakpoint = 0

        for i in range(0, len(songdict)):
            added_at = datetime.strptime(songdict[i]["added_at"], "%Y-%m-%dT%H:%M:%SZ")
            difference = datetime.now() - added_at
            dayDifference = difference.days
            if dayDifference <= 91:
                breakpoint = i
                print(songdict[i]["name"])
                break
        
        short_song_dict = songdict[0:breakpoint]
        
        return short_song_dict

    
    # Funktion die zwei Playlists vergleicht und die fehlenden Songs (es wird angenommen, dass immer nur die
    # gleiche Playlist neue Elemente bekommen wird und diese der anderen fehlen werden) dann als Liste mit uris ausgibt
    def playlist_comparison(self, realplaylist, backupplaylist):
        addList = []
        
        backupurilist = []
        for song in backupplaylist:
            backupurilist.append(song["uri"])

        for song in realplaylist:
            if song["uri"] not in backupurilist:
                addList.append(song["uri"])

        return addList
