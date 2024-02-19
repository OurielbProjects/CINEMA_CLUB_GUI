# Graphical User Interface. Here i make my Graphical Inteface with all these settings.

from PySide2 import QtWidgets, QtCore
from movie import get_movies               # I imported my functions from the API
from movie import Movie


# In this Class you will found my GUI settings, options, buttons and more.
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cinema Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()                                  # Line Edit
        self.btn_addMovie = QtWidgets.QPushButton("Add a movie")                    # I set the button to "Add a Movie" as i Wrote
        self.lw_movies = QtWidgets.QListWidget()                                    #list widget
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)    #make the possibility to select few rows to delete and not one by one.
        self.btn_removeMovies = QtWidgets.QPushButton("Remove movie(s)")  


        self.main_layout.addWidget(self.le_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.lw_movies)
        self.main_layout.addWidget(self.btn_removeMovies)

# this function make the connection between the widgets and the methods.
    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)   # add the option to add a movie with click on enter and not only from pressing the button.


    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)


    def add_movie(self):
        movie_title = self.le_movieTitle.text()

# this if condition will check if the user has written something, for not add empty row in my list.
        if not movie_title:             
            return False  

        movie = Movie(title=movie_title)
        resultat = movie.add_to_movies() 
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.lw_movies.addItem(lw_item)

        self.le_movieTitle.setText("")

# the remove function.
    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))
           


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()        