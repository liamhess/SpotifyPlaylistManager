import datetime
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
