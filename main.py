from internet import *
from api_calls import *
from logic import *

i = Internet()
a = ApiCalls(i.give_valid_access_token())
l = Logic()

# test playlist id = 60QjB7v7V8If58q661ZzOj
# echte drip drop playlist id = 6NYUUALff1pcZRJHaLpvRA


# print(a.get_playlist_items("60QjB7v7V8If58q661ZzOj"))
# print("\n\n\n")
# print(a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA"))
# print(a.remove_songs_from_playlist([{'name': 'Do You Want My Love', 'added_at': '2022-12-09T14:42:59Z', 'uri': 'spotify:track:3KPhaCvEPAKmwgYd8LARFe'}]))

# print(a.is_track_favorite([{'name': 'Do You Want My Love', 'added_at': '2022-12-09T14:42:59Z', 'uri': 'spotify:track:3KPhaCvEPAKmwgYd8LARFe'},{'name': 'Champagner', 'added_at': '2022-12-09T14:42:59Z', 'uri': 'spotify:track:4tfwHz3WpIbjKIsuuuTiEy'}]))
# print(l.favorite_dict_adder(a.get_playlist_items("60QjB7v7V8If58q661ZzOj")))

print(l.time_dict_shortener(a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA")))