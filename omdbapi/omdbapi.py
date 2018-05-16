import json
import requests


class MovieSearch:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_movie(self, title, plot=None):
        self.url = f'http://www.omdbapi.com/?t={title}&y=&plot={plot}&r=json&apikey={self.api_key}'
        self.response = requests.get(self.url)
        self.values = json.loads(self.response.text)

    def all(self):
        for k, v in self.values.items():
            print(k, ':', v)

    def get(self, item):
        return self.values[item.title()]
