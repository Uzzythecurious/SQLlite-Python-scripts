import csv
import re

counter = 0

# ask user for what title they want to see the count for
# string = input("title?: ").strip().upper()

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["title"].strip().upper()
        # two different methods for checking if office is in the title.
        # if "OFFICE" in title:
        # if  re.search("OFFICE", title):
        # check if the string contains office or the office and must begin with either of those words or end with either of those words hence ^ $
        if re.search("^(OFFICE|THE OFFICE)$", title):
        # check if userinput string in title.
        # if string in title:
            counter += 1

print(f"Number of people who like The Office: {counter}")