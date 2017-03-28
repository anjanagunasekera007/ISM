import csv
inventorylist = []

def creteitemdetailist():
    with open('./datasets/ITEM_FULL_LIST.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            inventorylist.append(transaction)
            print transaction
            print type(transaction)

print "BEIGN"
creteitemdetailist()
print "END"