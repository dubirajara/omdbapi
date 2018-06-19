# omdbapi python library.
[![Build Status](https://travis-ci.org/dubirajara/omdbapi.svg?branch=master)](https://travis-ci.org/dubirajara/omdbapi)
[![Updates](https://pyup.io/repos/github/dubirajara/omdbapi/shield.svg)](https://pyup.io/repos/github/dubirajara/omdbapi/)
[![Python 3](https://pyup.io/repos/github/dubirajara/omdbapi/python-3-shield.svg)](https://pyup.io/repos/github/dubirajara/omdbapi/)
[![codecov](https://codecov.io/gh/dubirajara/omdbapi/branch/master/graph/badge.svg)](https://codecov.io/gh/dubirajara/omdbapi)

Example build and distribution python projects - [Pytools](http://www.python.pro.br) course.

Used [The Open Movie Database](http://www.omdbapi.com) api to build a python lib and distribution in [pypi](https://pypi.org/project/omdbapi/).

## How to use?

#### Before, you must be request free the omdbapi api key [here](http://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0x0euvR%2FzVv1jLU3mGetH4R3kWtYKWACCaYcfoP1IY8g%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU5GG7XylwYou%2BzznFv7FbZmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulN6vYN8IikxxqwtGWTciOwQ4e4xie4N992dlfbpyqd1D&at=freeAcct&Email=)

Install the library:
```python
>>> pip install omdbapi
```

import the library and get movie, passing api key and title as parameter, default return short plot:
```python
>>> from omdbapi.movie_search import GetMovie

>>> movie = GetMovie('your api key', 'star wars')
```

Or can set full plot as parameter:
```python
>>> movie = GetMovie('your api key', 'star wars', 'full')
```

Get all data movie json format:
```python
>>> movie.get_all_data()

{'Title': 'Star Wars: Episode IV - A New Hope',
 'Year': '1977',
 'Rated': 'PG',
 'Released': '25 May 1977',
 'Runtime': '121 min',
 'Genre': 'Action, Adventure, Fantasy',
 'Director': 'George Lucas',
 'Writer': 'George Lucas',
 'Actors': 'Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing',
 'Plot': "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
 'Language': 'English',
 'Country': 'USA',
 'Awards': 'Won 6 Oscars. Another 50 wins & 28 nominations.',
 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.6/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '93%'},
  {'Source': 'Metacritic', 'Value': '90/100'}],
 'Metascore': '90',
 'imdbRating': '8.6',
 'imdbVotes': '1,057,823',
 'imdbID': 'tt0076759',
 'Type': 'movie',
 'DVD': '21 Sep 2004',
 'BoxOffice': 'N/A',
 'Production': '20th Century Fox',
 'Website': 'http://www.starwars.com/episode-iv/',
 'Response': 'True'}
```

Get values using keys as parameter:
```python
>>> movie.get_data('Director', 'Actors', 'Awards')

{'Director': 'George Lucas',
 'Actors': 'Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing',
 'Awards': 'Won 6 Oscars. Another 50 wins & 28 nominations.'}
```
