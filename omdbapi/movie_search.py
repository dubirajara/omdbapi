import json
import requests


class GetMovie:
    def __init__(self, api_key, title, plot=None):
        """
        instantiate the class, passing api key and title as parameter.

        :param api_key: ombdapi key
        :param title: title movie
        :param plot: optional, description plot, default return short plot or set full.

        :Example:
        m = MovieSearch('your api key', 'title movie')
        :Example:
        m = MovieSearch('your api key', 'title movie' 'full')
        """
        self.title = title
        self.api_key = api_key
        self.url = f'http://www.omdbapi.com/?t={self.title}&y=&plot={plot}&r=json&apikey={self.api_key}'
        self.response = requests.get(self.url)
        self.values = json.loads(self.response.text)

    def __repr__(self):
        return f"GetMovie('{self.api_key}', '{self.title}')"

    def get_all_data(self):
        """
        Get all data movie, key: value

        :Example:
        m.get_all_data()
        """
        if self.values['Response'] == 'True':
            return self.values
        else:
            print(self.values['Error'])

    def get_data(self, *args):
        """
        Get values passing keys as parameter.

        :param *args: items data key

        :Example:
        m.get_data('Director', 'Actors')
        """
        items = {item: self.values.get(item, 'key not found!') for item in args}
        return items

