import csv

with open('groceries.csv', 'rb') as f:
     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
     for row in reader:
         print row