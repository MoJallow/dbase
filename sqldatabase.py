#import csv library for opening and reading a csv file
import csv
from cs50 import SQL

open("gross_movies_db.db" , "w").close()

db = SQL("sqlite:///gross_movies_db.db")

db.execute("CREATE TABLE movies(id INTEGER , title TEXT , PRIMARY KEY(id))")
db.execute("CREATE TABLE movie_genres(movie_gen_id INTEGER , gen_id INTEGER , PRIMARY KEY(gen_id), FOREIGN KEY(movie_gen_id) REFERENCES movies(id)")
db.execute("CREATE TABLE genres(movie_id INTEGER , genre TEXT , PRIMARY KEY(movie_id),FOREIGN KEY(movie_id) REFERENCES movie_genres(gen_id))")

with open("gross movies.csv" , "r") as file:
	reader = csv.DictReader(file)

	for row in reader:
		title = row["Film"].strip().upper()

		id = db.execute("INSERT INTO movies (title) VALUES(?)" , title)
        
		for genre in row["Genre"].split(" , "):
				genre = genre.strip().upper()
				genres_id = db.execute("INSERT INTO movie_genres(movie_gen_id) VALUES((SELECT id FROM movies WHERE title = ? ))" , title)
    			db.execute("INSERT INTO genres (movie_id , genre) VALUES ((SELECT movie_gen_id FROM movie_genres WHERE movie_gen_id = ?) , ? )" , genres_id , genre)