from omdbapi.movie_search import GetMovie


def test_instance():
    get_movie = GetMovie('your api key', 'title movie')
    assert get_movie, get_movie.url is not None


# def test_get_all_data():
#     get_movie = GetMovie('11111', 'star wars')
#     assert get_movie.get_all_data() is None
#
#
# def test_get_data():
#     get_movie = GetMovie('11111', 'star wars')
#     item = get_movie.get_data('Plot')
#     assert 'key not found!' == item['Plot']
