
import datetime
from reviews.models import Movie

def load_movies():
    data = [
        {"title": "The Shawshank Redemption", "director": "Frank Darabont", "release_date": "1994-09-22", "genre": "Drama", "rating": 9.3},
        {"title": "The Godfather", "director": "Francis Ford Coppola", "release_date": "1972-03-24", "genre": "Crime", "rating": 9.2},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "release_date": "2008-07-18", "genre": "Action", "rating": 9.0},
        {"title": "12 Angry Men", "director": "Sidney Lumet", "release_date": "1957-04-10", "genre": "Drama", "rating": 8.9},
        {"title": "Schindler's List", "director": "Steven Spielberg", "release_date": "1993-12-15", "genre": "Biography", "rating": 8.9},
        {"title": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson", "release_date": "2003-12-17", "genre": "Adventure", "rating": 8.9},
        {"title": "Pulp Fiction", "director": "Quentin Tarantino", "release_date": "1994-10-14", "genre": "Crime", "rating": 8.9},
        {"title": "The Good, the Bad and the Ugly", "director": "Sergio Leone", "release_date": "1966-12-23", "genre": "Western", "rating": 8.8},
        {"title": "Fight Club", "director": "David Fincher", "release_date": "1999-10-15", "genre": "Drama", "rating": 8.8},
        {"title": "Forrest Gump", "director": "Robert Zemeckis", "release_date": "1994-07-06", "genre": "Drama", "rating": 8.8},
        {"title": "Inception", "director": "Christopher Nolan", "release_date": "2010-07-16", "genre": "Action", "rating": 8.8},
        {"title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", "release_date": "1999-03-31", "genre": "Sci-Fi", "rating": 8.7},
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_date": "2001-12-19", "genre": "Adventure", "rating": 8.8},
        {"title": "The Lord of the Rings: The Two Towers", "director": "Peter Jackson", "release_date": "2002-12-18", "genre": "Adventure", "rating": 8.7},
        {"title": "Goodfellas", "director": "Martin Scorsese", "release_date": "1990-09-19", "genre": "Crime", "rating": 8.7},
        {"title": "One Flew Over the Cuckoo's Nest", "director": "Milos Forman", "release_date": "1975-11-19", "genre": "Drama", "rating": 8.7},
        {"title": "Seven Samurai", "director": "Akira Kurosawa", "release_date": "1954-04-26", "genre": "Adventure", "rating": 8.6},
        {"title": "The Silence of the Lambs", "director": "Jonathan Demme", "release_date": "1991-02-14", "genre": "Thriller", "rating": 8.6},
        {"title": "City of God", "director": "Fernando Meirelles, Kátia Lund", "release_date": "2002-02-08", "genre": "Crime", "rating": 8.6},
        {"title": "Se7en", "director": "David Fincher", "release_date": "1995-09-22", "genre": "Crime", "rating": 8.6},
        {"title": "The Usual Suspects", "director": "Bryan Singer", "release_date": "1995-08-16", "genre": "Crime", "rating": 8.5},
        {"title": "Léon: The Professional", "director": "Luc Besson", "release_date": "1994-09-14", "genre": "Action", "rating": 8.5},
        {"title": "The Green Mile", "director": "Frank Darabont", "release_date": "1999-12-10", "genre": "Drama", "rating": 8.5},
        {"title": "Parasite", "director": "Bong Joon-ho", "release_date": "2019-05-30", "genre": "Comedy", "rating": 8.6},
        {"title": "The Lion King", "director": "Roger Allers, Rob Minkoff", "release_date": "1994-06-15", "genre": "Animation", "rating": 8.5},
        {"title": "Back to the Future", "director": "Robert Zemeckis", "release_date": "1985-07-03", "genre": "Adventure", "rating": 8.5},
        {"title": "Gladiator", "director": "Ridley Scott", "release_date": "2000-05-05", "genre": "Action", "rating": 8.5},
        {"title": "Memento", "director": "Christopher Nolan", "release_date": "2000-10-11", "genre": "Thriller", "rating": 8.4},
        {"title": "Apocalypse Now", "director": "Francis Ford Coppola", "release_date": "1979-08-15", "genre": "Drama", "rating": 8.4},
        {"title": "The Departed", "director": "Martin Scorsese", "release_date": "2006-10-06", "genre": "Crime", "rating": 8.4},
        {"title": "The Prestige", "director": "Christopher Nolan", "release_date": "2006-10-20", "genre": "Drama", "rating": 8.4},
        {"title": "Whiplash", "director": "Damien Chazelle", "release_date": "2014-10-10", "genre": "Drama", "rating": 8.5},
        {"title": "The Shining", "director": "Stanley Kubrick", "release_date": "1980-05-23", "genre": "Horror", "rating": 8.4},
        {"title": "The Great Dictator", "director": "Charlie Chaplin", "release_date": "1940-10-15", "genre": "Comedy", "rating": 8.4},
        {"title": "Reservoir Dogs", "director": "Quentin Tarantino", "release_date": "1992-10-23", "genre": "Crime", "rating": 8.3},
        {"title": "A Clockwork Orange", "director": "Stanley Kubrick", "release_date": "1971-12-19", "genre": "Crime", "rating": 8.3},
        {"title": "The Intouchables", "director": "Olivier Nakache, Éric Toledano", "release_date": "2011-11-02", "genre": "Comedy", "rating": 8.5},
        {"title": "Modern Times", "director": "Charlie Chaplin", "release_date": "1936-02-06", "genre": "Comedy", "rating": 8.5},
        {"title": "Once Upon a Time in the West", "director": "Sergio Leone", "release_date": "1968-12-21", "genre": "Western", "rating": 8.5},
        {"title": "Psycho", "director": "Alfred Hitchcock", "release_date": "1960-09-08", "genre": "Horror", "rating": 8.5},
        {"title": "Casablanca", "director": "Michael Curtiz", "release_date": "1942-11-26", "genre": "Drama", "rating": 8.5},
        {"title": "City Lights", "director": "Charlie Chaplin", "release_date": "1931-03-07", "genre": "Comedy", "rating": 8.5},
        {"title": "The Seventh Seal", "director": "Ingmar Bergman", "release_date": "1957-02-18", "genre": "Drama", "rating": 8.5},
        {"title": "Lawrence of Arabia", "director": "David Lean", "release_date": "1962-12-16", "genre": "Adventure", "rating": 8.5},
        {"title": "The Treasure of the Sierra Madre", "director": "John Huston", "release_date": "1948-01-08", "genre": "Adventure", "rating": 8.5},
        {"title": "To Kill a Mockingbird", "director": "Robert Mulligan", "release_date": "1962-12-25", "genre": "Drama", "rating": 8.5},
        {"title": "The Apartment", "director": "Billy Wilder", "release_date": "1960-06-15", "genre": "Comedy", "rating": 8.5},
        {"title": "Rear Window", "director": "Alfred Hitchcock", "release_date": "1954-08-01", "genre": "Mystery", "rating": 8.5},
        {"title": "Braveheart", "director": "Mel Gibson", "release_date": "1995-05-24", "genre": "Drama", "rating": 8.5},
        {"title": "The Big Lebowski", "director": "Joel Coen, Ethan Coen", "release_date": "1998-03-06", "genre": "Comedy", "rating": 8.1},
        {"title": "The Big Sleep", "director": "Howard Hawks", "release_date": "1946-08-23", "genre": "Crime", "rating": 8.0},
        {"title": "Sunset Boulevard", "director": "Billy Wilder", "release_date": "1950-08-10", "genre": "Drama", "rating": 8.4},
        {"title": "The Maltese Falcon", "director": "John Huston", "release_date": "1931-01-01", "genre": "Crime", "rating": 8.1},
        {"title": "Inglourious Basterds", "director": "Quentin Tarantino", "release_date": "2009-08-21", "genre": "War", "rating": 8.3},
        {"title": "Django Unchained", "director": "Quentin Tarantino", "release_date": "2012-12-25", "genre": "Western", "rating": 8.4},
        {"title": "The Wolf of Wall Street", "director": "Martin Scorsese", "release_date": "2013-12-25", "genre": "Biography", "rating": 8.2}
    ]

    for item in data:
        try:
            release_date = datetime.datetime.strptime(item['release_date'], '%Y-%m-%d').date()
        except ValueError as e:
            print(f"Error parsing date {item['release_date']}: {e}")
            release_date = None

        Movie.objects.create(
            title=item['title'],
            director=item['director'],
            release_date=release_date,
            genre=item['genre'],
            rating=item['rating']
        )

    if __name__ == "__main__":
        load_movies()