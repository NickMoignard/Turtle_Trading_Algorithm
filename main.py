import csv
from datetime import datetime

path = ""
file = open(path, newline='') 
reader = csv.reader(file)

header = next(reader)

data = []

for row in reader:
    x, y, z = "", "", ""
    # store each column in a variable
    data.append([x, y, z])

# compute stuff

# TODO: replace with functional path
returns_path = "?:\code\data/google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Column Title", "Another Column Title"])

for i in range(len(data)-1):
    # TODO: Perform MATH and store in variables
    todays_row = data[i]
    b, c = row[1], row[2]

    result = b * c 
    formatted_date = todays_row[0].strftime('%d/%m/%Y')
    writer.writerow([formatted_date, b, c])

