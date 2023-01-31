import csv

# intialize dictionary
titles = {}

# open csv in read and set reader function with dictreader
with open('favourites.csv', 'r') as file:
    reader = csv.DictReader(file)

# sanitise and canonicalize input
    for row in reader:
        title = row["title"].upper().strip()


# check to see if the title is in the dictionary if so add 1 to its value and if not add it into the dictionary and 1 for the first occurance
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1

# print out a list of title keys and count values and sort by highest value of title key
    for title in sorted(titles, key =lambda title: titles[title], reverse = True):
        print (title, titles[title])

