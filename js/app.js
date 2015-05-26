// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.tile', function (event) {
    $('#trailer').foundation('reveal', 'open');
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id'),
        sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
});

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

function showTiles(container) {
    $(container + ' .tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });
}

// Animate in the movies when the page loads
$(document).ready(showMovies);
$(document).on('click', '#movies a', showMovies);
$(document).on('click', '#tvshows a', showTvshows);