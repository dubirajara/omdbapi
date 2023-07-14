from dataclasses import dataclass, field

import requests


class GetMovieException(Exception):
    """GetMovie Exception"""


@dataclass
class GetMovie:
    """
    instantiate the class, passing api key.

    :param api_key: ombdapi key

    :Example:
    movie = GetMovie(api_key='your api key')
    """
    api_key: str
    values: dict = field(default_factory=dict)

    def get_movie(self, title, plot=None):
        """
        Get all data movie.
        :param title: movie title to search
        :param plot: by default return short plot
        :Example:
        movie.get_movie(title='Interstellar', plot='full')
        """
        url = 'http://www.omdbapi.com/'
        payload = {'t': title, 'plot': plot, 'r': 'json', 'apikey': self.api_key}
        result = requests.get(url, params=payload).json()

        if result.pop('Response') == 'False':
            raise GetMovieException(result['Error'])

        for key, value in result.items():
            key = key.lower()
            setattr(self, key, value)
            self.values[key] = value

        return self.values

    def get_data(self, *args):
        """
        Get values passing keys as parameter.

        :param *args: items data key

        :Example:
        movie.get_data('Director', 'Actors')
        """
        items = {item.lower(): self.values.get(item.lower(), 'key not found!') for item in args}

        return items
