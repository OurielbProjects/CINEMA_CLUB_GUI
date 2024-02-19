# NOA'S API ! here you will found all my functions I will use in cine_app file.


import os
import json
import logging



# I make this Path to give me the possibility to read and write in my json file
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")



def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies
       
class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

# this is my Read function
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

# this is my Write function
    def _write_movies(self, movies ):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent = 4) 


    def add_to_movies(self):
        movies = self._get_movies()

        # this part of code is checking if the movie i'm gonna add already exist in my list or not. If yes, I get a special notifications.
        if self.title not in movies:              
            movies.append(self.title)
            self._write_movies(movies)
            return True

        else:
            logging.warning(f"The movie {self.title} is already downloaded.")
            return False

        # remove function. there is a check too. If the movie i suggested to remove not in my list, i get a notification.
    def remove_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True

        else:
            logging.warning(f"The movie {self.title} is not in the list.")
            return False     


if __name__ == "__main__"   :
    #m = Movie("Sponge bob")
    #m.remove_from_movies()  
    movies = get_movies()
    print(movies)


#m = Movie("Le seigneur des Anneaux")
#print(m._write_movies(["Batman", "Fast & Furious"]))     