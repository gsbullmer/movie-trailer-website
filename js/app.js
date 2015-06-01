// Pause the video when the modal is closed
$(document).on('click', '.close-reveal-modal, .reveal-modal-bg', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.tile.movie', function (event) {
    var movieTitle = $(this).attr('data-movie-title'),
        movieTrailerId = $(this).attr('data-movie-youtube-id'),
        sourceUrl = 'http://www.youtube.com/embed/' + movieTrailerId + '?autoplay=1&html5=1',
        movieRating = '<span class="label success radius">' + $(this).attr('data-movie-rating') + '</span>',
        movieCast = $(this).attr('data-movie-cast'),
        movieRuntime = $(this).attr('data-movie-runtime');
    
    $('#movieTitle').empty().append(movieTitle + ' ' + movieRating);
    $('#movieCast').empty().append('Staring: ' + movieCast);
    $('#movieRuntime').empty().append('Runtime: ' + movieRuntime);
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
    
    $('#trailer').foundation('reveal', 'open');
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.tile.tv-show', function (event) {
    var rating = $(this).attr('data-rating'),
        tvShowTitle = $(this).attr('data-trailer-title'),
        tvShowRating = '<span class="label success radius">' + rating + '</span>',
        tvShowCast = $(this).attr('data-cast'),
        tvShowPlot = $(this).attr('data-plot'),
        tvShowPoster = $(this).attr('data-poster-img');
    
    $('#tvShowPoster').empty().append('<img src="' + tvShowPoster + '"/>');
    $('#tvShowTitle').empty().append(tvShowTitle + ' ' + tvShowRating);
    $('#tvShowCast').empty().append('Staring: ' + tvShowCast);
    $('#tvShowPlot').empty().append(tvShowPlot);
    
    $('#tvShowInfo').foundation('reveal', 'open');
});

function showTiles(container) {
    $(container + ' .tile').hide().first().show("fast", function showNext() {
        console.log($(window).width());
        if ($(this).next("div").hasClass('clearfix')) {
            // Check to see if screen should have large column layout
            if ($(this).next("div").hasClass('large')) {
                $(this).next("div").show(0, showNext);
            // Check to see if screen should have medium column layout
            } else if ($(this).next("div").hasClass('medium') && $(window).width() <= 1007) {
                $(this).next("div").show(0, showNext);
            } else {
                $(this).next("div").hide(0, showNext);
            }
        } else {
            $(this).next("div").show("fast", showNext);
        }
    });
}

function showMovies() {
    $('#movies').addClass('active');
    $('#tvshows').removeClass('active');

    $('#tv-tiles').addClass('hide');
    $('#movie-tiles').removeClass('hide');
    
    showTiles('#movie-tiles');
}

function showTvshows() {
    $('#tvshows').addClass('active');
    $('#movies').removeClass('active');

    $('#tv-tiles').removeClass('hide');
    $('#movie-tiles').addClass('hide');
    
    showTiles('#tv-tiles');
}

// Animate in the movies when the page loads
$(document).ready(showMovies);
$(document).on('click', '#movies a', showMovies);
$(document).on('click', '#tvshows a', showTvshows);

$(window).resize(function() {
    console.log($(window).width());
    if ($(window).width() <= 1007) {
        $('.clearfix.medium').show();
    } else {
        $('.clearfix.medium').hide();
    }
});