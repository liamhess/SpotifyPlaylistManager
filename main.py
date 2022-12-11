from internet import *
from api_calls import *

i = Internet()
a = ApiCalls(i.give_valid_access_token())

# i.renew_access_token()
# print(i.access_token_check())

# print(i.give_valid_access_token())

print(a.get_playlist_items())