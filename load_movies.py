import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Movie_Critic.settings')
django.setup()

# Import the Movie model
from reviews.models import Movie

# List of movies to add
movies = [
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "release_date": "1994-10-14", "genre": "Drama",
     "rating": 9.3},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "release_date": "1972-03-24", "genre": "Crime",
     "rating": 9.2},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "release_date": "2008-07-18", "genre": "Action",
     "rating": 9.0},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "release_date": "1994-10-14", "genre": "Crime",
     "rating": 8.9},
    {"title": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson",
     "release_date": "2003-12-17", "genre": "Adventure", "rating": 8.9},
    {"title": "Schindler's List", "director": "Steven Spielberg", "release_date": "1993-12-15", "genre": "Biography",
     "rating": 8.9},
    {"title": "Fight Club", "director": "David Fincher", "release_date": "1999-10-15", "genre": "Drama", "rating": 8.8},
    {"title": "Forrest Gump", "director": "Robert Zemeckis", "release_date": "1994-07-06", "genre": "Drama",
     "rating": 8.8},
    {"title": "Inception", "director": "Christopher Nolan", "release_date": "2010-07-16", "genre": "Action",
     "rating": 8.8},
    {"title": "The Matrix", "director": "The Wachowskis", "release_date": "1999-03-31", "genre": "Science Fiction",
     "rating": 8.7},
    {"title": "The Empire Strikes Back", "director": "Irvin Kershner", "release_date": "1980-05-21",
     "genre": "Adventure", "rating": 8.7},
    {"title": "Goodfellas", "director": "Martin Scorsese", "release_date": "1990-09-19", "genre": "Biography",
     "rating": 8.7},
    {"title": "One Flew Over the Cuckoo's Nest", "director": "Milos Forman", "release_date": "1975-11-19",
     "genre": "Drama", "rating": 8.7},
    {"title": "The Silence of the Lambs", "director": "Jonathan Demme", "release_date": "1991-02-14", "genre": "Crime",
     "rating": 8.6},
    {"title": "Se7en", "director": "David Fincher", "release_date": "1995-09-22", "genre": "Crime", "rating": 8.6},
    {"title": "It's a Wonderful Life", "director": "Frank Capra", "release_date": "1946-12-20", "genre": "Drama",
     "rating": 8.6},
    {"title": "Saving Private Ryan", "director": "Steven Spielberg", "release_date": "1998-07-24", "genre": "Drama",
     "rating": 8.6},
    {"title": "Interstellar", "director": "Christopher Nolan", "release_date": "2014-11-07", "genre": "Science Fiction",
     "rating": 8.6},
    {"title": "Parasite", "director": "Bong Joon Ho", "release_date": "2019-05-30", "genre": "Thriller", "rating": 8.6},
    {"title": "The Green Mile", "director": "Frank Darabont", "release_date": "1999-12-10", "genre": "Crime",
     "rating": 8.6},
    {"title": "Léon: The Professional", "director": "Luc Besson", "release_date": "1994-11-18", "genre": "Action",
     "rating": 8.5},
    {"title": "The Usual Suspects", "director": "Bryan Singer", "release_date": "1995-08-16", "genre": "Crime",
     "rating": 8.5},
    {"title": "Harakiri", "director": "Masaki Kobayashi", "release_date": "1962-09-15", "genre": "Drama",
     "rating": 8.6},
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "release_date": "2001-07-20", "genre": "Animation",
     "rating": 8.6},
    {"title": "The Pianist", "director": "Roman Polanski", "release_date": "2002-09-25", "genre": "Biography",
     "rating": 8.5},
    {"title": "Gladiator", "director": "Ridley Scott", "release_date": "2000-05-05", "genre": "Action", "rating": 8.5},
    {"title": "American History X", "director": "Tony Kaye", "release_date": "1998-10-30", "genre": "Drama",
     "rating": 8.5},
    {"title": "The Departed", "director": "Martin Scorsese", "release_date": "2006-10-06", "genre": "Crime",
     "rating": 8.5},
    {"title": "Whiplash", "director": "Damien Chazelle", "release_date": "2014-10-10", "genre": "Drama", "rating": 8.5},
    {"title": "The Intouchables", "director": "Olivier Nakache, Éric Toledano", "release_date": "2011-11-02",
     "genre": "Biography", "rating": 8.5},
    {"title": "Back to the Future", "director": "Robert Zemeckis", "release_date": "1985-07-03", "genre": "Adventure",
     "rating": 8.5},
    {"title": "Terminator 2: Judgment Day", "director": "James Cameron", "release_date": "1991-07-03",
     "genre": "Action", "rating": 8.5},
    {"title": "The Prestige", "director": "Christopher Nolan", "release_date": "2006-10-20", "genre": "Drama",
     "rating": 8.5},
    {"title": "The Lion King", "director": "Roger Allers, Rob Minkoff", "release_date": "1994-06-24",
     "genre": "Animation", "rating": 8.5},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson",
     "release_date": "2001-12-19", "genre": "Adventure", "rating": 8.8},
    {"title": "The Lord of the Rings: The Two Towers", "director": "Peter Jackson", "release_date": "2002-12-18",
     "genre": "Adventure", "rating": 8.7},
    {"title": "Braveheart", "director": "Mel Gibson", "release_date": "1995-05-24", "genre": "Biography",
     "rating": 8.4},
    {"title": "Inglourious Basterds", "director": "Quentin Tarantino", "release_date": "2009-08-21",
     "genre": "Adventure", "rating": 8.3},
    {"title": "Memento", "director": "Christopher Nolan", "release_date": "2000-09-05", "genre": "Mystery",
     "rating": 8.4},
    {"title": "Joker", "director": "Todd Phillips", "release_date": "2019-10-04", "genre": "Crime", "rating": 8.4},
    {"title": "Apocalypse Now", "director": "Francis Ford Coppola", "release_date": "1979-08-15", "genre": "Drama",
     "rating": 8.4},
    {"title": "Alien", "director": "Ridley Scott", "release_date": "1979-05-25", "genre": "Horror", "rating": 8.4},
    {"title": "Aliens", "director": "James Cameron", "release_date": "1986-07-18", "genre": "Action", "rating": 8.4},
    {"title": "WALL·E", "director": "Andrew Stanton", "release_date": "2008-06-27", "genre": "Animation",
     "rating": 8.4},
    {"title": "A Clockwork Orange", "director": "Stanley Kubrick", "release_date": "1971-12-19", "genre": "Crime",
     "rating": 8.3},
    {"title": "Oldboy", "director": "Park Chan-wook", "release_date": "2003-11-21", "genre": "Action", "rating": 8.4},
    {"title": "Toy Story", "director": "John Lasseter", "release_date": "1995-11-22", "genre": "Animation", "rating": 8.3},
]


for movie_data in movies:
    movie = Movie(
        title=movie_data["title"],
        director=movie_data["director"],
        release_date=datetime.strptime(movie_data["release_date"], "%Y-%m-%d").date(),
        genre=movie_data["genre"],
        rating=movie_data["rating"]
    )
    movie.save()

print("Movies have been added to the database.")