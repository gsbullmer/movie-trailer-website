# Movie Trailer Website Generator
This is the first of several projects for the Udacity Full-Stack Web Developer Nanodegree program.

## Purpose of this project
Write a server-side script in python to store a list of movies and tv shows, including related poster art, trailer URL, and other information. The script will then generate a static web page allowing visitors to browse the titles, watch trailers, and see other related information.

## How to use this project
### Dependencies
#### Python
This project was built with Python 2.7. Download it [here](https://www.python.org/downloads/).

### Configuration
1. In `video_db.py`, add your favorite movies and tv shows.
2. Add `Movie` instances to the `movies` array and `TvShow` instances to the `tvshows` array.
3. Run the `video_db.py` script.
4. If the page doesn't open automatically, open `index.html`.

#### Movie class
The Movie class takes two arguments:
- IMDb ID
- YouTube URL

The IMDb ID can be found in the IMDb page url. This is usually after `title/` and starts with `tt`.

#### TvShow class
The TvShow class takes one argument:
- IMDb ID

The IMDb ID can be found in the IMDb page url. This is usually after the `title/` and starts with `tt`.

## To-Do
- [x] Create keys.py to store api keys
- [ ] ~~Replace omdb api calls with tmdbsimple~~
- [ ] Further design website
- [ ] Pagination?
- [ ] Finalize documentation

## Developement Notes
I decided to scrap using the tmdbsimple api for this project. There are limits on how many requests it can handle in a given time, and that severely limited the usefulness in this project. Titles were making several requests and was resulting in 429 errors.