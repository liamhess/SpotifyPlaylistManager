from internet import *
from api_calls import *
from logic import *

i = Internet()
a = ApiCalls(i.give_valid_access_token())
l = Logic()

# test playlist id = 60QjB7v7V8If58q661ZzOj
# echte drip drop playlist id = 6NYUUALff1pcZRJHaLpvRA
# drip drop backup playlist id = 7kEpthO12IIpyOSuXnxPXD

print(l.playlist_comparison(realplaylist=a.get_playlist_items("6NYUUALff1pcZRJHaLpvRA"), backupplaylist=a.get_playlist_items("7kEpthO12IIpyOSuXnxPXD")))