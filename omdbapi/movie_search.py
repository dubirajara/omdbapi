from dataclasses import dataclass

import requests

url = 'http://www.omdbapi.com/'


@dataclass
class GetMovie(object):
    """
    instantiate the class, passing api key and title as parameter.

    :param api_key: ombdapi key
    :param title: title movie
    :param plot: optional, description plot, default return short plot or set full.

    :Example:
    m = GetMovie('your api key', 'title movie')
    :Example:
    m = GetMovie('your api key', 'title movie', 'full')
    """
    title: str
    api_key: str
    plot: str = None

    def __post_init__(self):
        payload = {'t': self.title, 'plot': self.plot, 'r': 'json', 'apikey': self.api_key}
        self.values = requests.get(url, params=payload).json()

    def get_all_data(self):
        """
        Get all data movie, key: value
        :Example:
        m.get_all_data()
        """
        if self.values['Response'] == 'True':
            return self.values
        else:
            return self.values['Error']

    def get_data(self, *args):
        """
        Get values passing keys as parameter.

        :param *args: items data key

        :Example:
        m.get_data('Director', 'Actors')
        """
        items = {item: self.values.get(item, 'key not found!') for item in args}

        return items
