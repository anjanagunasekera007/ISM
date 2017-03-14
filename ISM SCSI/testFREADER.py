
import time
from Item_Class import Item
from Item_Class import FullItem
import sys
import csv

inventorylist = []
itemlist = []
objectlist = []


# def createitemdetailslist():
#     with open("./datasets/category list.csv") as f:
#         ib = f.read().splitlines()
#         print len(ib)
#         # sys.exit(89)
#         time.sleep(2)
#         for i in ib:
#             print i
#             inventorylist.append(i)


def creteitemdetailist():
    with open('./datasets/category list.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            inventorylist.append(transaction)
            print transaction
            print type(transaction)


def createobjectlist():
    counter = 1
    for it in inventorylist:
        print it
        print type(it)
        I = FullItem(counter,it[0], it[1], it[2])
        objectlist.append(I)
        counter = counter +1

creteitemdetailist()
createobjectlist()

time.sleep(2)
for obj in objectlist:
    print str(obj.id) + " : " + obj.name + " : " + obj.description + " : " + obj.category + " : : : : " + str(obj.soldQ2)

# sys.exit(345)
# for it in inventorylist:
#     print it
#     print type(it)
#     I = Item(it[0],it[1],it[2])
#     itemlist.append(I)

# sys.exit(43)
time.sleep(2)
print "priting items"
for u in itemlist:
    print u.name + " " + u.description + " : " + u.category