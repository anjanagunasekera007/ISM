from Item_Class import Item
import csv
import time
import itertools
import sys

inventorylist = []

transactionT1 = []
transactionT2 = []
transactionT3 = []
transactionT4 = []


objectlist = []


oilist = []

Q1 = []
Q2 = []
Q3 = []
Q4 = []

def createInventoryList():
    with open("./datasets/all_items.txt") as f:
        ib = f.read().splitlines()
        print len(ib)
        time.sleep(2)
        for i in ib:
            print i
            inventorylist.append(i)

def createobjectlist():
    for inventoryItem in inventorylist:
        I = Item(inventoryItem)
        objectlist.append(I)

def writeToFile():
    thefile = open('./datasets/itemsales.txt', 'w')
    for item in objectlist:
        thefile.write(item.name+","+str(item.soldQ1)+","+str(item.soldQ2)+","+str(item.soldQ3)+"\n")

def createQ1Transactions():
    with open('./datasets/Q1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q1.append(transaction)

def createQ2Transactions():
    with open('./datasets/Q2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q2.append(transaction)

def createQ3Transactions():
    with open('./datasets/Q3.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q3.append(transaction)

def createQ4Transactions():
    with open('./datasets/Q4.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q4.append(transaction)


def Q1sales():
    for purchase in Q1:
        for purchasedItem in purchase:
            for obj in objectlist:
                if purchasedItem == obj.name:
                    print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
                    obj.soldQ1 = obj.soldQ1 + 1

def Q2sales():
    for purchase in Q2:
        for purchasedItem in purchase:
            for obj in objectlist:
                if purchasedItem == obj.name:
                    print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
                    obj.soldQ2 = obj.soldQ2 + 1



def Q3sales():
    for purchase in Q3:
        for purchasedItem in purchase:
            for obj in objectlist:
                if purchasedItem == obj.name:
                    print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
                    obj.soldQ3 = obj.soldQ3 + 1


def Q4sales():
    for purchase in Q4:
        for purchasedItem in purchase:
            for obj in objectlist:
                if purchasedItem == obj.name:
                    print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
                    obj.soldQ4 = obj.soldQ4 + 1


def createTotal():
    for objects in objectlist:
        objects.soldTotal = objects.soldQ1 + objects.soldQ2 + objects.soldQ3 + objects.soldQ4


createInventoryList()
createobjectlist()

createQ1Transactions()
createQ2Transactions()
createQ3Transactions()
createQ4Transactions()



print "ALL LISTS CREATED "

Q1sales()
time.sleep(2)
Q2sales()
time.sleep(2)
Q3sales()
time.sleep(2)
Q4sales()
time.sleep(2)

createTotal()
print "PRINING Q1"
for l in Q1:
    print l
    print type(l)
time.sleep(2)

print "ITEM LIST"
for item in inventorylist:
    print item
time.sleep(2)

print "OBJECT LIST FINAL"
for j in objectlist:
    print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
sys.exit(54)