import csv

# open the csv file in read mode
with open ('favourites.csv', 'r') as file:
    # use the dictreader function on the file
    reader = csv.DictReader(file)

    # initiate titles list
    titles = []

    # create for loop to add title into titles list only if it's not already there (to avoid repeats)
    for row in reader:
        # clean user input by uppercasing and striping whitespace
        title = row["title"].upper().strip()
        if not title in titles:
            titles.append(title)

    # print out the titles in an sorted fashion
    for title in sorted(titles):
        print(title)
