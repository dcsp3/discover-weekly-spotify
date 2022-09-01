import json
import requests

from datetime import date

from refresh import Refresh
from secrets import spotify_user_id, discover_weekly_id

class DiscoverWeekly:
    def __init__(self):
        self.refresh = Refresh()
        self.spotify_token = self.refresh.refresh()
        self.user_id = spotify_user_id
        self.discover_weekly_id = discover_weekly_id
        self.today_date = str(date.today())
        self.new_playlist_id = ""
        self.tracks = []

    def main(self):
        self.create_playlist()

        print('getting tracks from playlist...')

        query = f"https://api.spotify.com/v1/playlists/{self.discover_weekly_id}/tracks"

        response = requests.get(query, headers={
            "Content-Type": "applications/json",
            "Authorization": f"Bearer {self.spotify_token}"})

        response_json = response.json()

        for i in response_json['items']:
            self.tracks.append(i["track"]["uri"])

        self.add_to_playlist(','.join(self.tracks))

    def create_playlist(self):
        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        request_body =  json.dumps({
            "name": f"Discover Weekly ({self.today_date[-2:] + '/' + self.today_date[-5:-3]})",
            "description": "Your weekly mixtape of fresh music. Enjoy new music and deep cuts picked for you. Updates every Monday. Automated by python."
        })

        response = requests.post(query, data=request_body, headers={
                "Content-Type": "applications/json",
                "Authorization": f"Bearer {self.spotify_token}"})

        response_json = response.json()
        self.new_playlist_id = response_json["id"]

    def add_to_playlist(self, tracks):        
        print("Adding songs.....")
        query = f"https://api.spotify.com/v1/playlists/{self.new_playlist_id}/tracks?uris={tracks}"

        requests.post(query, headers={
                "Content-Type": "applications/json",
                "Authorization": f"Bearer {self.spotify_token}"})


if __name__ == '__main__':
    obj = DiscoverWeekly()
    obj.main()
