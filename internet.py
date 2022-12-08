import requests
import json

# access_token und refresh_token aus data.txt auslesen und in variablen schreiben
access_token = ""
refresh_token = ""
with open("data.txt", "r") as f:
    content = json.loads(f.read())
    access_token = content["access_token"]
    refresh_token = content["refresh_token"]


# Funktion um zu checken, ob access_token noch gültig ist, oder ob er refreshed werden muss
# True = gültig, False = ungültig
def token_check():
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": "Bearer " + access_token,
    }
    r = requests.get(url=url, headers=headers)
    if r.status_code == 401:
        return False
    else:
        return True


# Funktion um access_token mit refresh_token zu erneuern
def token_refresh():
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    headers = {
        "Authorization": "Basic NmI4NjUzNTJiZWY1NDljMDg4ZmYzMzNiYTYwYjVhMGY6NmFjYWVjNjIxNDNkNDQxODk2OWY3NzhmYTcwODRiZTM="
    }

    r = requests.post(url=url, data=data, headers=headers)

    content_dir = r.json();
    access_token = content_dir["access_token"]

    # falls es einen neuen refresh_token gibt, wird der in Variable und danach in data.txt gespeichert
    if new_refresh_token_given():
        refresh_token = content_dir["refresh_token"]

    # neuen access_token und jenachdem auch refresh_token in data.txt schreiben
    with open("data.txt", "w") as f:
        file_dir = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        f.write(json.dumps(file_dir))


# Funktion die checkt, ob in einem dictionary ein "refresh_token" Wert gegeben ist
# konkreter usecase hier: ob in token_refresh() ein neuer refresh_token gegeben wird
def new_refresh_token_given(dict):
    value = False;
    if "refresh_token" in dict:
        value = True;
    return value