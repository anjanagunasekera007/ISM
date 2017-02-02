import csv

with open('DATA.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print row

    # cl = createCl(readCSV)
    # print(cl)