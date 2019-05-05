from unittest.mock import Mock

import pytest

from omdbapi import movie_search


@pytest.fixture
def get_movie(mocker):
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
    get_mock = mocker.patch('omdbapi.movie_search.requests.get')
    get_mock.return_value = resp_mock
    data_movie = movie_search.GetMovie(title='star wars', api_key='12345')
    return data_movie


@pytest.mark.parametrize(
    'movie',
    ('Title', 'Awards', 'Year', 'Genre', 'Writer', 'Response', 'Actors', 'Director')
)
def test_get_all_data(movie, get_movie):
    data_movie = get_movie.get_all_data()
    assert movie in data_movie


def test_repr():
    movie = movie_search.GetMovie(api_key='12345', title='star wars')
    assert repr(movie) == "GetMovie(title='star wars', api_key='12345', plot=None)"


@pytest.mark.parametrize(
    'movie',
    ('Title', 'Awards', 'Year')
)
def test_get_data(movie, get_movie):
    data_movie = get_movie.get_data('Title', 'Awards', 'Year')
    assert movie in data_movie


def test_data_key_not_found(get_movie):
    data_movie = get_movie.get_data('Plot')
    assert data_movie['Plot'] == 'key not found!'


def test_get_data_invalid():
    url = movie_search.GetMovie(title='star wars', api_key='1111')
    assert url.get_all_data() == 'Invalid API key!'
