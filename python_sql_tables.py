# Imports titles and genres from CSV into a SQLite database

import cs50
import csv

# Create database
open("favourites8.db", "w").close()
db = cs50.SQL("sqlite:///favourites8.db")

# Create tables
db.execute("CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres (show_id INTEGER, genres TEXT NOT NULL, FOREIGN KEY(show_id) REFERENCES shows(id))")

# Open CSV file
with open("favourites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file
    for row in reader:

        # Canoncalize title
        title = row["title"].strip().upper()

        # Insert title
        show_id = db.execute("INSERT INTO shows (title) VALUES(?)", title)

        # Insert genres
        for genres in row["genres"].split(", "):

            db.execute("INSERT INTO genres (show_id, genres) VALUES(?, ?)", show_id, genres)