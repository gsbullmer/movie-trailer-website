import webbrowser
import json
import urllib2

class Video():
    """ This class provides a way to store basic video information """
    
    def __init__(self, imdb_id):
        # Make JSON request using OMDb
        # http://www.omdbapi.com/

        # Found information on how to make a JSON request
        # http://stackoverflow.com/questions/2817481/how-do-i-request-and-process-json-with-python
        self.video_data = json.load(urllib2.urlopen("http://www.omdbapi.com/?i=" + imdb_id + "&plot=full&r=json"))
        
        # Found information on 
        # http://stackoverflow.com/questions/3224268/python-unicode-encode-error
        self.title = self.video_data["Title"].encode('ascii', 'xmlcharrefreplace')
        self.poster_image_url = self.video_data["Poster"]
        self.cast = self.video_data["Actors"].encode('ascii', 'xmlcharrefreplace')
        self.rating = self.video_data["Rated"].encode('ascii', 'xmlcharrefreplace')
        self.year = self.video_data["Year"].encode('ascii', 'xmlcharrefreplace')
    
class Movie(Video):
    """ This class provides a way to store movie related information """

    def __init__(self, imdb_id, youtube_url):
        Video.__init__(self, imdb_id)
        
        self.runtime = self.video_data["Runtime"].encode('ascii', 'xmlcharrefreplace')
        self.trailer_youtube_url = youtube_url

class TvShow(Video):
    """ This class provides a way to store tv show related information """
    
    def __init__(self, imdb_id):
        Video.__init__(self, imdb_id)
        
        self.plot = str.replace(self.video_data["Plot"].encode('ascii', 'xmlcharrefreplace'), "\"", "&quot;")