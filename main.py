from internet import *
from api_calls import *

i = Internet()
a = ApiCalls(i.give_valid_access_token())



# print(a.get_playlist_items())
print(a.remove_songs_from_playlist())