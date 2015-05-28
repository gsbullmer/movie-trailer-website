from py import media_center
from py.media import Movie, TvShow

# Using OMdb API to gather movie information from IMDb using IMDb id
# http://www.omdbapi.com/
oldboy = Movie("tt0364569","https://www.youtube.com/watch?v=D89OHw0VsYM")
spirited_away = Movie("tt0245429","https://www.youtube.com/watch?v=ByXuk9QqQkk")
great_new_wonderful = Movie("tt0402230","https://www.youtube.com/watch?v=0RwZG7N-DvI")
scott_pilgrim = Movie("tt0446029","https://www.youtube.com/watch?v=7wd5KEaOtm4")
burn_after_reading = Movie("tt0887883","https://www.youtube.com/watch?v=eMWu6i7l5ec")
once = Movie("tt0907657","https://www.youtube.com/watch?v=I6xIF92OUos")
wish_i_was_here = Movie("tt2870708","https://www.youtube.com/watch?v=4HP2fm9zNAE")
hitchhikers_guide = Movie("tt0371724","https://www.youtube.com/watch?v=MbGNcoB2Y4I")
boondock_saints = Movie("tt0144117","https://www.youtube.com/watch?v=x04M-C0pF-U")
serenity = Movie("tt0379786","https://www.youtube.com/watch?v=w8JNjmK5lfk")
pacific_rim = Movie("tt1663662","https://www.youtube.com/watch?v=rkOy1C8eX6o")
pans_labyrinth = Movie("tt0457430","https://www.youtube.com/watch?v=E7XGNPXdlGQ")

movies = [oldboy, spirited_away, great_new_wonderful, scott_pilgrim, burn_after_reading, once, wish_i_was_here, hitchhikers_guide, boondock_saints, serenity, pacific_rim, pans_labyrinth]

# Using OMdb API to gather tv show information from IMDb using IMDb id
# http://www.omdbapi.com/
firefly = TvShow(1437)
it_crowd = TvShow("tt0487831")
castle = TvShow("tt1219024")
at_midnight = TvShow("tt3279494")
agents_of_sheild = TvShow("tt2364582")
stargate_sg1 = TvShow("tt0118480")
eureka = TvShow("tt0796264")
yu_yu_hakusho = TvShow("tt0185133")
ncis_no = TvShow("tt3560084")
grimm = TvShow("tt1830617")
mythbusters = TvShow("tt0383126")
dr_who = TvShow("tt0436992")
californication = TvShow("tt0904208")
game_of_thrones = TvShow("tt0944947")

tvshows = [firefly, it_crowd, castle, at_midnight, agents_of_sheild, stargate_sg1, eureka, yu_yu_hakusho, ncis_no, grimm, mythbusters, dr_who, californication, game_of_thrones]

media_center.create_page(movies, tvshows)