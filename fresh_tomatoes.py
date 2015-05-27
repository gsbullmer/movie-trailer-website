import webbrowser
import os
import re

# Styles for the page
main_page_head = '''
<!doctype html>
<html class="no-js" lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Fresh Tomatoes!</title>
        
        <!-- Zurb Foundation 5 framework -->
        <link rel="stylesheet" href="css/normalize.css">
        <link rel="stylesheet" href="css/foundation.css"/>
        
        <!-- Page-specific styles -->
        <link rel="stylesheet" href="css/app.css">

        <script src="js/vendor/modernizr.js"></script>
    </head>
'''

# The main page layout and title bar
main_page_content = '''
    <body>
        <!-- TV Show Info Modal -->
        <div id="tvShowInfo" class="reveal-modal" data-reveal aria-labelledby="showTitle" aria-hidden="true" role="dialog">
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
        <div id="trailer" class="reveal-modal" data-reveal aria-labelledby="trailerTitle" aria-hidden="true" role="dialog">
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
                        <h1><a href="#">Fresh Tomatoes Movie Trailers</a></h1>
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
movie_tile_content = '''
            <div class="medium-4 columns end tile movie text-center" data-movie-youtube-id="{movie_youtube_id}" data-movie-title="{movie_title}" data-movie-cast="{movie_cast}" data-movie-runtime="{movie_runtime}" data-movie-rating="{movie_rating}">
                <img src="{poster_image_url}" width="220" height="342">
                <h3>{movie_title}</h3>
                <h5 class="subheader">{release_year}</h5>
                <span class="label success radius">{movie_rating}</span>
            </div>
'''

# A single tv show entry html template
tvshow_tile_content = '''
            <div class="medium-4 columns end tile tv-show text-center" data-trailer-title="{tvshow_title}" data-cast="{tvshow_cast}" data-plot="{tvshow_plot}" data-rating="{tvshow_rating}" data-poster-img="{poster_image_url}">
                <img src="{poster_image_url}" width="220" height="342">
                <h3>{tvshow_title}</h3>
                <h5 class="subheader">{release_year}</h5>
                <span class="label success radius">{tvshow_rating}</span>
            </div>
'''

# Fixes vertical alignment issues with Foundation grid layouts
clearfix_content = '''
            <div class="clearfix"></div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    # Start the movie-tiles row
    content = '''
        <div id="movie-tiles" class="row hide">
    '''
    columns = 3 # Total number of columns per row
    counter = 0
    for movie in movies:
        # Insert the clearfix between rows
        if counter == columns:
            counter = 1
            content += clearfix_content
        else:
            counter += 1
            
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        movie_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            movie_runtime = movie.runtime,
            release_year = movie.year,
            movie_cast = movie.cast,
            movie_rating = movie.rating,
            movie_youtube_id = movie_youtube_id
        )
    
    # Close row
    content += '''
        </div>
    '''
    return content

def create_tv_tiles_content(tvshows):
    # The HTML content for this section of the page
    # Start the tv-tiles row
    content = '''
        <div id="tv-tiles" class="row hide">
    '''
    columns = 3 # Total number of columns per row
    counter = 0
    for tvshow in tvshows:
        # Insert the clearfix between rows
        if counter == columns:
            counter = 1
            content += clearfix_content
        else:
            counter += 1

        # Append the tile for the tv show with its content filled in
        content += tvshow_tile_content.format(
            tvshow_title = tvshow.title,
            poster_image_url = tvshow.poster_image_url,
            tvshow_plot = tvshow.plot,
            release_year = tvshow.year,
            tvshow_cast = tvshow.cast,
            tvshow_rating = tvshow.rating
        )
    
    # Close row
    content += '''
        </div>
    '''
    return content

def open_page(movies, tvshows):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(
        movie_tiles = create_movie_tiles_content(movies),
        tv_tiles = create_tv_tiles_content(tvshows)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
