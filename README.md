# omdbapi python library.
[![Build Status](https://travis-ci.org/dubirajara/omdbapi.svg?branch=master)](https://travis-ci.org/dubirajara/omdbapi)
[![Updates](https://pyup.io/repos/github/dubirajara/omdbapi/shield.svg)](https://pyup.io/repos/github/dubirajara/omdbapi/)
[![Python 3](https://pyup.io/repos/github/dubirajara/omdbapi/python-3-shield.svg)](https://pyup.io/repos/github/dubirajara/omdbapi/)
[![codecov](https://codecov.io/gh/dubirajara/omdbapi/branch/master/graph/badge.svg)](https://codecov.io/gh/dubirajara/omdbapi)

Python lib to get movie, series, episode data from the Open Movie Database (OMDb) api.
Example build and distribution python projects - [Pytools](http://www.python.pro.br) course.

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

>>> movie = GetMovie(api_key='your api key')
```

Get all data movie json format:
```python
>>> movie.get_movie(title='Interstellar')

{'title': 'Interstellar',
 'year': '2014',
 'rated': 'PG-13',
 'released': '07 Nov 2014',
 'runtime': '169 min',
 'genre': 'Adventure, Drama, Sci-Fi',
 'director': 'Christopher Nolan',
 'writer': 'Jonathan Nolan, Christopher Nolan',
 'actors': 'Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow',
 'plot': "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
 'language': 'English',
 'country': 'USA, UK, Canada',
 'awards': 'Won 1 Oscar. Another 43 wins & 148 nominations.',
 'poster': 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg',
 'ratings': [{'Source': 'Internet Movie Database', 'Value': '8.6/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '72%'},
  {'Source': 'Metacritic', 'Value': '74/100'}],
 'metascore': '74',
 'imdbrating': '8.6',
 'imdbvotes': '1,569,520',
 'imdbid': 'tt0816692',
 'type': 'movie',
 'dvd': '24 May 2016',
 'boxoffice': '$188,020,017',
 'production': 'Lynda Obst Productions, Syncopy',
 'website': 'N/A',
 'response': 'True'}

```
Or can set full plot as parameter:
```python
>>> movie.get_movie(title='Interstellar', plot='full')
{'title': 'Interstellar',
 'year': '2014',
 'rated': 'PG-13',
 'released': '07 Nov 2014',
 'runtime': '169 min',
 'genre': 'Adventure, Drama, Sci-Fi',
 'director': 'Christopher Nolan',
 'writer': 'Jonathan Nolan, Christopher Nolan',
 'actors': 'Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow',
 'plot': "Earth's future has been riddled by disasters, famines, and droughts. There is only one way to ensure mankind's survival: Interstellar travel. A newly discovered wormhole in the far reaches of our solar system allows a team of astronauts to go where no man has gone before, a planet that may have the right environment to sustain human life.",
 'language': 'English',
 'country': 'USA, UK, Canada',
 'awards': 'Won 1 Oscar. Another 43 wins & 148 nominations.',
 'poster': 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg',
 'ratings': [{'Source': 'Internet Movie Database', 'Value': '8.6/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '72%'},
  {'Source': 'Metacritic', 'Value': '74/100'}],
 'metascore': '74',
 'imdbrating': '8.6',
 'imdbvotes': '1,569,520',
 'imdbid': 'tt0816692',
 'type': 'movie',
 'dvd': '24 May 2016',
 'boxoffice': '$188,020,017',
 'production': 'Lynda Obst Productions, Syncopy',
 'website': 'N/A',
 'response': 'True'}

```

Get values using keys as parameter:
```python
>>> movie.get_data('director', 'actors', 'awards', 'plot')

{'director': 'Christopher Nolan',
 'actors': 'Ellen Burstyn, Matthew McConaughey, Mackenzie Foy, John Lithgow',
 'awards': 'Won 1 Oscar. Another 43 wins & 148 nominations.',
 'plot': "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."}
```
