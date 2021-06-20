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
    movie = movie_search.GetMovie(api_key='12345')
    return movie


@pytest.mark.parametrize(
    'expected',
    ('title', 'awards', 'year', 'genre', 'writer', 'response', 'actors', 'director')
)
def test_get_all_data(expected, get_movie):
    movie = get_movie.get_movie(title='star wars')
    assert expected in movie


def test_repr():
    movie = movie_search.GetMovie(api_key='12345')
    assert repr(movie) == "GetMovie(api_key='12345', values=None)"


@pytest.mark.parametrize(
    'expected',
    ('title', 'awards', 'year')
)
def test_get_data(expected, get_movie):
    get_movie.get_movie(title='star wars')
    data_movie = get_movie.get_data('Title', 'Awards', 'Year')
    assert expected in data_movie


def test_data_key_not_found(get_movie):
    get_movie.get_movie(title='star wars')
    data_movie = get_movie.get_data('Plot')
    assert data_movie['plot'] == 'key not found!'


def test_get_data_invalid():
    movie = movie_search.GetMovie(api_key='1111')
    assert movie.get_movie(title='star wars') == 'Invalid API key!'
