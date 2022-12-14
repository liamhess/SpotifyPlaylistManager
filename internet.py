import requests
import json


# Klasse, die sich um Ablaufen und Erneuern der Tokens kümmert
class Internet:


    def __init__(self):
        # access_token und refresh_token aus data.txt auslesen und in variablen schreiben
        with open("data.txt", "r") as f:
            content = json.loads(f.read())
            self.access_token = content["access_token"]
            self.refresh_token = content["refresh_token"]


    # Funktion um zu checken, ob access_token noch gültig ist, oder ob er refreshed werden muss
    # True = gültig, False = ungültig
    def access_token_check(self):
        url = "https://api.spotify.com/v1/me"
        headers = {
            "Authorization": "Bearer " + self.access_token,
        }
        r = requests.get(url=url, headers=headers)
        if r.status_code == 401:
            return False
        else:
            return True


    # Funktion die checkt, ob in einem dictionary ein "refresh_token" Wert gegeben ist
    # konkreter usecase hier: ob in token_refresh() ein neuer refresh_token gegeben wird
    def new_refresh_token_given(self, dict):
        if "refresh_token" in dict:
            return True
        else: return False


    # Funktion um access_token mit refresh_token zu erneuern
    def renew_access_token(self):
        url = "https://accounts.spotify.com/api/token"
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
        }
        headers = {
            "Authorization": "Basic NmI4NjUzNTJiZWY1NDljMDg4ZmYzMzNiYTYwYjVhMGY6NmFjYWVjNjIxNDNkNDQxODk2OWY3NzhmYTcwODRiZTM="
        }

        r = requests.post(url=url, data=data, headers=headers)

        content_dir = r.json();
        self.access_token = content_dir["access_token"]

        # falls es einen neuen refresh_token gibt, wird der in Variable und danach in data.txt gespeichert
        if self.new_refresh_token_given(content_dir):
            refresh_token = content_dir["refresh_token"]

        # neuen access_token und jenachdem auch refresh_token in data.txt schreiben
        with open("data.txt", "w") as f:
            file_dir = {
                "access_token":  self.access_token,
                "refresh_token": self.refresh_token
            }
            f.write(json.dumps(file_dir))


    # Funktion, die alle Internet Methods nun vereint, um wenn aufgerufen immer einen gültigen access_token rauszugeben
    def give_valid_access_token(self):
        if self.access_token_check():
            return self.access_token
        else:
            self.renew_access_token()
            if self.access_token_check():
                return self.access_token
            else:
                print("access_token_renewal didn't work")