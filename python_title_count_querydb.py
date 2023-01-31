import csv

from cs50 import SQL

db = SQL("sqlite:///favourites.db")

title = input("Title: ").strip()

rows = db.execute("SELECT COUNT(*) AS counter FROM favourites WHERE title LIKE ?", title)

row = rows[0]

print(row["counter"])
