# Movie Trailer Website Generator
This is the first of several projects for the Udacity Full-Stack Web Developer Nanodegree program.

## Purpose of this project
Write a server-side script in python to store a list of movies and tv shows, including related poster art, trailer URL, and other information. The script will then generate a static web page allowing visitors to browse the titles, watch trailers, and see other related information.

## How to use this project
### Dependancies
#### Python
This project was build with Python 2.7. Download it [here](https://www.python.org/downloads/).

#### tmdbsimple
tmdbsimple is used to query The Movie DataBase to populate details for each movie and tv show.
To install with pip:

`pip install tmdbsimple`

For more information, check [here](https://github.com/celiao/tmdbsimple/).

### Configuration
1. In `video_db.py`, add your favorite movies and tv shows.
2. Add `Movie` instances to the `movies` array and `TvShow` instances to the `tvshows` array.
3. Run the `video_db.py` script.
4. If the page doesn't open automatically, open `index.html`.

#### Movie class
The Movie class takes two arguments:
- IMDb ID
- YouTube URL
The IMDb ID can be found in the IMDb page url. This is usually after the `title/` and starts with `tt`.

#### TvShow class
The TvShow class takes one argument:
- IMDb ID
The IMDb ID can be found in the IMDb page url. This is usually after the `title/` and starts with `tt`.

## To-Do
- [x] Create keys.py to store api keys
- [ ] Replace omdb api calls with tmdbsimple
- [ ] Further design website
- [ ] Finalize documentation
