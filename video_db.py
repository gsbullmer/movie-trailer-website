"""Database used to generate a static webpage displaying information
related to each title.
"""

from py import media_center
from py.media import Movie, TvShow


# Using OMdb API to gather movie information from IMDb using IMDb id
# http://www.omdbapi.com/
OLDBOY = Movie("tt0364569",
               "https://www.youtube.com/watch?v=D89OHw0VsYM")
SPIRITED_AWAY = Movie("tt0245429",
                      "https://www.youtube.com/watch?v=ByXuk9QqQkk")
GREAT_NEW_WONDERFUL = Movie("tt0402230",
                            "https://www.youtube.com/watch?v=0RwZG7N-DvI")
SCOTT_PILGRIM = Movie("tt0446029",
                      "https://www.youtube.com/watch?v=7wd5KEaOtm4")
BURN_AFTER_READING = Movie("tt0887883",
                           "https://www.youtube.com/watch?v=eMWu6i7l5ec")
ONCE = Movie("tt0907657",
             "https://www.youtube.com/watch?v=I6xIF92OUos")
WISH_I_WAS_HERE = Movie("tt2870708",
                        "https://www.youtube.com/watch?v=4HP2fm9zNAE")
HITCHHIKERS_GUIDE = Movie("tt0371724",
                          "https://www.youtube.com/watch?v=MbGNcoB2Y4I")
BOONDOCK_SAINTS = Movie("tt0144117",
                        "https://www.youtube.com/watch?v=x04M-C0pF-U")
SERENITY = Movie("tt0379786",
                 "https://www.youtube.com/watch?v=w8JNjmK5lfk")
PACIFIC_RIM = Movie("tt1663662",
                    "https://www.youtube.com/watch?v=rkOy1C8eX6o")
PANS_LABYRINTH = Movie("tt0457430",
                       "https://www.youtube.com/watch?v=E7XGNPXdlGQ")

MOVIES = [OLDBOY, SPIRITED_AWAY, GREAT_NEW_WONDERFUL, SCOTT_PILGRIM,
          BURN_AFTER_READING, ONCE, WISH_I_WAS_HERE, HITCHHIKERS_GUIDE,
          BOONDOCK_SAINTS, SERENITY, PACIFIC_RIM, PANS_LABYRINTH]

# Using OMdb API to gather tv show information from IMDb using IMDb id
# http://www.omdbapi.com/
FIREFLY = TvShow("tt0303461")
IT_CROWD = TvShow("tt0487831")
CASTLE = TvShow("tt1219024")
AT_MIDNIGHT = TvShow("tt3279494")
AGENTS_OF_SHEILD = TvShow("tt2364582")
STARGATE_SG1 = TvShow("tt0118480")
EUREKA = TvShow("tt0796264")
YU_YU_HAKUSHO = TvShow("tt0185133")
NCIS_NO = TvShow("tt3560084")
GRIMM = TvShow("tt1830617")
MYTHBUSTERS = TvShow("tt0383126")
DR_WHO = TvShow("tt0436992")
CALIFORNICATION = TvShow("tt0904208")
GAME_OF_THRONES = TvShow("tt0944947")

TVSHOWS = [FIREFLY, IT_CROWD, CASTLE, AT_MIDNIGHT, AGENTS_OF_SHEILD,
           STARGATE_SG1, EUREKA, YU_YU_HAKUSHO, NCIS_NO, GRIMM, MYTHBUSTERS,
           DR_WHO, CALIFORNICATION, GAME_OF_THRONES]

media_center.create_page(MOVIES, TVSHOWS)
