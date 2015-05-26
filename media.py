import webbrowser
import json
import urllib

class Movie():
    """ This class provides a way to store movie related information """

    # Poster API key from http://beforethecode.com/projects/omdb/apikey.aspx
    POSTER_API_KEY = "4c859a2c"

    def __init__(self, movie_id, trailer_url):
        # Make JSON request using OMDb
        # http://www.omdbapi.com/

        # Found information on how to make a JSON request
        # http://stackoverflow.com/questions/2817481/how-do-i-request-and-process-json-with-python
        self.movie_data = json.load(urllib.urlopen("http://www.omdbapi.com/?apikey=" + Movie.POSTER_API_KEY + "&i=" + movie_id + "&plot=short&r=json"))

        self.title = self.movie_data["Title"]
        self.storyline = self.movie_data["Plot"]
        self.poster_image_url = self.movie_data["Poster"]
        self.year = self.movie_data["Year"]
        self.cast = self.movie_data["Actors"]
        self.rating = self.movie_data["Rated"]
        self.trailer_youtube_url = trailer_url
