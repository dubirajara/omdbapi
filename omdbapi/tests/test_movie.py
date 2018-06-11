from unittest.mock import Mock

import pytest

from omdbapi import movie_search


@pytest.mark.parametrize(
    'movie',
    ['Title', 'Awards', 'Year', 'Genre', 'Writer', 'Response', 'Actors', 'Director']
)
def test_get_movie(movie):
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'Title': 'Star Wars: Episode IV - A New Hope',
        'Year': '1977',
        'Genre': 'Action, Adventure, Fantasy',
        'Director': 'George Lucas',
        'Writer': 'George Lucas',
        'Actors': 'Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing',
        'Awards': 'Won 6 Oscars. Another 50 wins & 28 nominations.',
        'Response': 'True'
         }
    movie_search.requests.get = Mock(return_value=resp_mock)
    url = movie_search.GetMovie('12345', 'star wars').get_all_data()
    # assert url['Response'] == 'True'
    assert movie in url


def test_repr():
    assert repr(movie_search.GetMovie('12345', 'star wars')) == "GetMovie('12345', 'star wars')"


@pytest.mark.parametrize(
    'movie',
    ['Title', 'Awards', 'Year']
)
def test_get_data(movie):
    url = movie_search.GetMovie('12345', 'star wars').get_data('Title', 'Awards', 'Year')
    assert movie in url
