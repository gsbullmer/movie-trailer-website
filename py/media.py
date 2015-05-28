import os, json, urllib2, keys
import tmdbsimple as tmdb

tmdb.API_KEY = keys.TMDB_API_KEY

class Video():
    """ This class provides a way to store basic video information """
    
    def __init__(self, video):
        response = video.info()
        
        # Found information on 
        # http://stackoverflow.com/questions/3224268/python-unicode-encode-error
        self.title = video.title.encode('ascii', 'xmlcharrefreplace')
        self.cast = self.video.cast.encode('ascii', 'xmlcharrefreplace')
        
        response = video.images()
        self.poster_image_url = self.video.images
    
class Movie(Video):
    """ This class provides a way to store movie related information """

    def __init__(self, tmdb_id, youtube_url):
        self.movie = tmdb.Movies(tmdb_id)
                
        Video.__init__(self, self.movie)
        
        self.runtime = self.movie.runtime
        
        response = self.movie.releases()
        for c in self.movie.countries:
            if c['iso_3166_1'] == 'US':
                self.rating = c['certification']
                self.year = c['release_date']
        
        self.trailer_youtube_url = youtube_url

class TvShow():
    """ This class provides a way to store tv show related information """
    
    def __init__(self, tmdb_id):
        self.tv = tmdb.TV(tmdb_id)
                
        Video.__init__(self, self.tv)
        
        self.plot = str.replace(self.tv.overview.encode('ascii', 'xmlcharrefreplace'), "\"", "&quot;")
