# from Item_Class import Item
import csv
import time
from Item_Class import FullItem
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

#============
# newlist = []
# most = []
# least = []

#============
def createInventoryList():
    with open("D:/FYP/ISM SCSI/datasets/all_items.txt") as f:
        ib = f.read().splitlines()
        print len(ib)
        time.sleep(2)
        for i in ib:
            print i
            inventorylist.append(i)
#----------------------------------------------------------------
def createobjectlist():
    counter = 1
    for it in inventorylist:
        print it
        print type(it)
        I = FullItem(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9])
        #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
        objectlist.append(I)
        counter = counter +1
        # print "[][][][][][][][]][]][]["
        # sys.exit(99999)
#D:\FYP\ISM SCSI\datasets\
def creteitemdetailist():
    # with open('./datasets/full_item_detail_list.csv') as csvfile:
    with open('D:/FYP/ISM SCSI/datasets/full_item_detail_list.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            inventorylist.append(transaction)
            print transaction
            print type(transaction)
            # print str(len(transaction))
            # print ";;;;;;;;;;;;;;;;;;;;;"
            # sys.exit(99999)

#-------------------------------------------------------------------
def writeToFile():
    thefile = open('D:/FYP/ISM SCSI/datasets/itemsales.txt', 'w')
    for item in objectlist:
        thefile.write(item.name+","+str(item.soldQ1)+","+str(item.soldQ2)+","+str(item.soldQ3)+"\n")

def createQ1Transactions():
    with open('D:/FYP/ISM SCSI/datasets/Q1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q1.append(transaction)

def createQ2Transactions():
    with open('D:/FYP/ISM SCSI/datasets/Q2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q2.append(transaction)

def createQ3Transactions():
    with open('D:/FYP/ISM SCSI/datasets/Q3.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            Q3.append(transaction)

def createQ4Transactions():
    with open('D:/FYP/ISM SCSI/datasets/Q4.csv') as csvfile:
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

def returnSales():
    # createInventoryList()
    creteitemdetailist()
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

    for it in objectlist:
        print it.name + " : " + str(it.soldQ2)
    # sys.exit(698)
    return objectlist


# def returnmostandleast():
#
#     for j in newlist:
#         print type(newlist)
#         # print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
#         print j.name + " TOTAL SALES :" + str(j.soldTotal)
#     print str(len(newlist))

    # print "MOST SOLD ITEMS : "

def sortlist():
    newlist = sorted(objectlist, key=lambda x: x.soldTotal, reverse=True)
    for j in newlist:
        print type(newlist)
        print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
    return newlist
# def returnmostsold():
#     sortlist()
#     print "SORTED"
#     time.sleep(3)
#     most = newlist[0:5]
#     print "MOST SOLD ITEMS ARE : ========================= "
#     for j in most:
#         print j.name + " TOTAL SALES :" + str(j.soldTotal)
#     return most

# def retunleastsold():
#     sortlist()
#     print "SORTED"
#     time.sleep(3)
#     least = newlist[164:]
#     print "LEASE SOLD ITEMS ARE : ======================== "
#     for j in least:
#         print j.name + " TOTAL SALES :" + str(j.soldTotal)
#     return least
# createInventoryList()
# createobjectlist()
#
# createQ1Transactions()
# createQ2Transactions()
# createQ3Transactions()
# createQ4Transactions()
#
#
#
# print "ALL LISTS CREATED "
#
# Q1sales()
# time.sleep(2)
# Q2sales()
# time.sleep(2)
# Q3sales()
# time.sleep(2)
# Q4sales()
# time.sleep(2)
#
# createTotal()
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
# sys.exit(54)

# =========================================

def checkSales():
    for item_n in objectlist:
        if item_n.soldQ1==0 & item_n.soldQ2==0 & item_n.soldQ3==0 & item_n.soldQ4:
            print "SOLD"


# =============================================