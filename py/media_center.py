"""Generates Interactive Media Center static webpage.

From video_db.py, call create_page() with two arguments:
    - Array containing Movie objects
    - Array containing TvShow objects
"""

import os
import re
import webbrowser


# Styles for the page
MAIN_PAGE_HEAD = '''<!doctype html>
<html class="no-js" lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Interactive Media Center</title>
        
        <!-- Zurb Foundation 5 framework -->
        <link rel="stylesheet" href="css/normalize.css">
        <link rel="stylesheet" href="css/foundation.css"/>
        
        <!-- Page-specific styles -->
        <link rel="stylesheet" href="css/app.css">

        <script src="js/vendor/modernizr.js"></script>
    </head>
'''

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
    <body>
        <!-- TV Show Info Modal -->
        <div id="tvShowInfo" class="reveal-modal medium" data-reveal aria-labelledby="showTitle" aria-hidden="true" role="dialog">
            <h2 id="tvShowTitle"></h2>
            <div class="row">
                <div id="tvShowPoster" class="medium-4 columns">
                </div>
                <div class="medium-8 columns">
                    <p id="tvShowPlot"></p>
                    <p id="tvShowCast">Staring: </p>
                </div>
            </div>
            <a class="close-reveal-modal" aria-label="Close">&#215;</a>
        </div>
        
        <!-- Trailer Video Modal -->
        <div id="trailer" class="reveal-modal medium" data-reveal aria-labelledby="trailerTitle" aria-hidden="true" role="dialog">
            <h2 id="movieTitle"></h2>
            <div class="flex-video" id="trailer-video-container">
            </div>
            <p id="movieRuntime">Runtime: </p>
            <p id="movieCast">Staring: </p>
            <a class="close-reveal-modal" aria-label="Close">&#215;</a>
        </div>

        <!-- Main Page Content -->
        
        <!-- Zurb Foundation 5 Top Bar -->
        <div class="fixed contain-to-grid">
            <nav class="top-bar fixed" data-topbar role="navigation">
                <ul class="title-area">
                    <li class="name">
                        <h1><a href="#">Interactive Media Center</a></h1>
                    </li>
                    <!-- Remove the class "menu-icon" to get rid of menu icon. Take out "Menu" to just have icon alone -->
                    <li class="toggle-topbar menu-icon"><a href="#"><span>Menu</span></a></li>
                </ul>

                <section class="top-bar-section">
                    <!-- Right Nav Section -->
                    <ul class="right">
                        <li id="movies" class="active"><a href="#movies">Movies</a></li>
                        <li id="tvshows"><a href="#tv">TV Series</a></li>
                    </ul>
                </section>
            </nav>
        </div>
        
        <!-- Dynamically created tiles -->
        {movie_tiles}
        {tv_tiles}
        <!-- Zurb Foundation 5 framework -->
        <script src="js/vendor/jquery.js"></script>
        <script src="js/foundation.min.js"></script>
        
        <!-- Page-specific scripts -->
        <script src="js/app.js"></script>
        
        <!-- Zurb Foundation 5 framework -->
        <script>
            $(document).foundation();
        </script>
    </body>
</html>
'''

# A single movie entry html template
MOVIE_TILE_CONTENT = '''
            <div class="medium-6 large-3 columns end tile movie text-center" data-movie-youtube-id="{movie_youtube_id}" data-movie-title="{movie_title}" data-movie-cast="{movie_cast}" data-movie-runtime="{movie_runtime}" data-movie-rating="{movie_rating}">
                <img src="{poster_image_url}" width="250">
                <h3>{movie_title}</h3>
                <h5 class="subheader">{release_year}</h5>
                <span class="label success radius">{movie_rating}</span>
            </div>
'''

# A single tv show entry html template
TVSHOW_TILE_CONTENT = '''
            <div class="medium-6 large-3 columns end tile tv-show text-center" data-trailer-title="{tvshow_title}" data-cast="{tvshow_cast}" data-plot="{tvshow_plot}" data-rating="{tvshow_rating}" data-poster-img="{poster_image_url}">
                <img src="{poster_image_url}" width="250">
                <h3>{tvshow_title}</h3>
                <h5 class="subheader">{release_year}</h5>
                <span class="label success radius">{tvshow_rating}</span>
            </div>
'''

# Fixes vertical alignment issues with Foundation grid layouts
CLEARFIX_CONTENT_LARGE = '''
            <div class="clearfix large"></div>
'''

CLEARFIX_CONTENT_MEDIUM = '''
            <div class="clearfix medium"></div>
'''

def create_movie_tiles_content(movies):
    """Generates the html content for each Movie in movies."""

    # The HTML content for this section of the page
    # Start the movie-tiles row
    content = '''
        <div id="movie-tiles" class="row hide">
    '''
    columns = 4 # Total number of columns per row
    counter = 0
    for movie in movies:
        # Insert the clearfix between rows
        if counter == columns:
            counter = 1
            content += CLEARFIX_CONTENT_LARGE
        else:
            if counter == columns / 2:
                content += CLEARFIX_CONTENT_MEDIUM
            counter += 1

        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.get_trailer_youtube_url())
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         movie.get_trailer_youtube_url())
        movie_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.get_title(),
            poster_image_url=movie.get_poster_image_url(),
            movie_runtime=movie.get_runtime(),
            release_year=movie.get_year(),
            movie_cast=movie.get_cast(),
            movie_rating=movie.get_rating(),
            movie_youtube_id=movie_youtube_id
        )

    # Close row
    content += '''
        </div>
    '''
    return content

def create_tv_tiles_content(tvshows):
    """Generate the html content for each TvShow in tvshows."""

    # The HTML content for this section of the page
    # Start the tv-tiles row
    content = '''
        <div id="tv-tiles" class="row hide">
    '''
    columns = 4 # Total number of columns per row
    counter = 0
    for tvshow in tvshows:
        # Insert the clearfix between rows
        if counter == columns:
            counter = 1
            content += CLEARFIX_CONTENT_LARGE
        else:
            if counter == columns / 2:
                content += CLEARFIX_CONTENT_MEDIUM
            counter += 1

        # Append the tile for the tv show with its content filled in
        content += TVSHOW_TILE_CONTENT.format(
            tvshow_title=tvshow.get_title(),
            poster_image_url=tvshow.get_poster_image_url(),
            tvshow_plot=tvshow.get_plot(),
            release_year=tvshow.get_year(),
            tvshow_cast=tvshow.get_cast(),
            tvshow_rating=tvshow.get_rating()
        )

    # Close row
    content += '''
        </div>
    '''
    return content

def create_page(movies, tvshows):
    """Generates webpage with movies and tvshows content."""

    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies),
        tv_tiles=create_tv_tiles_content(tvshows)
    )

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
