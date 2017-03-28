import csv
import sys
import time
from Item_Category_Class import ItemC
from collections import defaultdict


print "BEGIN"

itemobjectlist = []
transactionlist = []
db = []
results = []

def read():
        with open("../DATASETS/category list.csv", 'rb') as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                # print row
                # print type(row)
                t = filter(None, row)
                # db.append(t)
                item = ItemC(t[0],t[1],t[2])
                print t
                print type(t)
                print str(len(t))
                print "COUNTER : " + str(counter)
                itemobjectlist.append(item)
                counter = counter +1



def readtransactionlist():
    print "reading transactions"
    with open("../DATASETS/item list.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            # f.append(row)
            print row
            transactionlist.append(row)
            # print row
            # print type(row)
            # t = filter(None, row)
            # print t

def replacce():
    print "replacing"
    for transaction in transactionlist:
        n = []
        print transaction
        for item in transaction:
            print item
            for iditem in itemobjectlist:
                if iditem.name == item:
                    print " ====================== match found"
                    n.append(iditem.categoryid)
        db.append(n)
read()
readtransactionlist()
replacce()

for i in xrange(len(db)):
    print str(i)