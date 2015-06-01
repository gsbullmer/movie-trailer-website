"""Video-related objects that hold relevant information."""

import json
import os
import urllib2


class Video(object):
    """ This class provides a way to store basic video information """

    def __init__(self, imdb_id):
        # Make JSON request using OMDb
        # http://www.omdbapi.com/

        # Found information on how to make a JSON request
        # http://stackoverflow.com/questions/2817481/how-do-i-request-and-process-json-with-python
        self._video_data = json.load(
            urllib2.urlopen("http://www.omdbapi.com/?i=" + imdb_id + "&plot=full&r=json"))

        self._set_cast(self._video_data["Actors"])
        self._set_poster_image(imdb_id, self._video_data["Poster"])
        self._set_rating(self._video_data["Rated"])
        self._set_title(self._video_data["Title"])
        self._set_year(self._video_data["Year"])

    def get_cast(self):
        """Return Video cast."""
        return self._title

    def _set_cast(self, data):
        """Set Video cast."""
        self._cast = data.encode('ascii', 'xmlcharrefreplace')

    def get_poster_image_url(self):
        """Return Video poster image url."""
        return self._poster_image_url

    def _set_poster_image(self, imdb_id, data):
        """Set Video poster image."""
        self._poster_image_url = "img/" + imdb_id + ".jpg"
        create_image(data, self._poster_image_url)

    def get_rating(self):
        """Return Video rating."""
        return self._rating

    def _set_rating(self, data):
        """Set Video rating."""
        self._rating = data.encode('ascii', 'xmlcharrefreplace')

    def get_title(self):
        """Return Video title."""
        return self._title

    def _set_title(self, data):
        """Set Video title."""
        self._title = data.encode('ascii', 'xmlcharrefreplace')

    def get_year(self):
        """Return Video year."""
        return self._year

    def _set_year(self, data):
        """Set Video year."""
        self._year = data.encode('ascii', 'xmlcharrefreplace')

class Movie(Video):
    """ This class provides a way to store movie related information """

    def __init__(self, imdb_id, youtube_url):
        Video.__init__(self, imdb_id)

        self._set_runtime(self._video_data["Runtime"])
        self._set_trailer_youtube_url(youtube_url)

    def get_runtime(self):
        """Return Movie runtime."""
        return self._runtime

    def _set_runtime(self, data):
        """Set Movie runtime."""
        self._runtime = data.encode('ascii', 'xmlcharrefreplace')

    def get_trailer_youtube_url(self):
        """Return Movie trailer youtube url."""
        return self._trailer_youtube_url

    def _set_trailer_youtube_url(self, url):
        """Set Movie trailer youtube url."""
        self._trailer_youtube_url = url

class TvShow(Video):
    """ This class provides a way to store tv show related information """

    def __init__(self, imdb_id):
        Video.__init__(self, imdb_id)

        self._set_plot(self._video_data["Plot"])

    def get_plot(self):
        """Return TvShow plot."""
        return self._plot

    def _set_plot(self, data):
        """Set TvShow plot."""
        _plot = data.encode('ascii', 'xmlcharrefreplace')
        self._plot = str.replace(_plot, "\"", "&quot;")


def create_image(url, file_path):
    """Create an image if none exists."""

    # Check to see if file exists first
    if not os.path.isfile(file_path):

        # Create or overwrite the output file
        output_file = open(file_path, 'wb')

        # Get image data
        image = urllib2.urlopen(url)

        # Output the file
        output_file.write(image.read())
        output_file.close()
    else:
        print "Image already exists."
