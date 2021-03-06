# omdbapi python library.

[![PyPI version](https://badge.fury.io/py/omdbapi.svg)](https://badge.fury.io/py/omdbapi)
[![Build Status](https://travis-ci.org/dubirajara/omdbapi.svg?branch=master)](https://travis-ci.org/dubirajara/omdbapi)
[![codecov](https://codecov.io/gh/dubirajara/omdbapi/branch/master/graph/badge.svg)](https://codecov.io/gh/dubirajara/omdbapi)

Python lib to get movie, series, episode data from the Open Movie Database (OMDb) api.
Example build and distribution python projects - [Pytools](https://www.python.pro.br/modulos/descricao/pytools/) course.

Used [The Open Movie Database](http://www.omdbapi.com) api to build a python lib and distribution in [pypi](https://pypi.org/project/omdbapi/).

## How to use? 

**IMPORTANT**: Requires Python 3.7 or newer. To works with python 3.6 must install the versión 0.5.1.

#### Before, you must be request free the omdbapi api key [here](http://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0x0euvR%2FzVv1jLU3mGetH4R3kWtYKWACCaYcfoP1IY8g%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU5GG7XylwYou%2BzznFv7FbZmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulN6vYN8IikxxqwtGWTciOwQ4e4xie4N992dlfbpyqd1D&at=freeAcct&Email=)

Install the library, Python 3.7 or newer:
```python
>>> pip install omdbapi
```
To works with python 3.6 must install the versión 0.5.1
```python
>>> pip install omdbapi==0.5.1
```

import the library and get movie, passing api key and title as parameter, default return short plot:
```python
>>> from omdbapi.movie_search import GetMovie

>>> movie = GetMovie(title='Interstellar', api_key='your api key')
```

Or can set full plot as parameter:
```python
>>> movie = GetMovie(title='Interstellar', api_key='your api key', plot='full')
```


Get all data movie json format:
```python
>>> movie.get_all_data()

{'Title': 'Interstellar',
 'Year': '2014',
 'Rated': 'PG-13',
 'Released': '07 Nov 2014',
 'Runtime': '169 min',
 'Genre': 'Adventure, Drama, Sci-Fi',
 'Director': 'Christopher Nolan',
 'Writer': 'Jonathan Nolan, Christopher Nolan',
 'Actors': 'Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow',
 'Plot': "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
 'Language': 'English',
 'Country': 'USA, UK, Canada',
 'Awards': 'Won 1 Oscar. Another 43 wins & 143 nominations.',
 'Poster': 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg',
 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.6/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '72%'},
  {'Source': 'Metacritic', 'Value': '74/100'}],
 'Metascore': '74',
 'imdbRating': '8.6',
 'imdbVotes': '1,275,886',
 'imdbID': 'tt0816692',
 'Type': 'movie',
 'DVD': '31 Mar 2015',
 'BoxOffice': '$158,737,441',
 'Production': 'Paramount Pictures',
 'Website': 'http://www.InterstellarMovie.com/',
 'Response': 'True'}
```

Get values using keys as parameter:
```python
>>> movie.get_data('Director', 'Actors', 'Awards', 'Plot')

{'Director': 'Christopher Nolan',
 'Actors': 'Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow',
 'Awards': 'Won 1 Oscar. Another 43 wins & 143 nominations.',
 'Plot': "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."}
```
