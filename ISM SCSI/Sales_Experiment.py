from Item_Class import Item
import csv
import time

inventorylist = []
transactionlist = []
objectlist = []


def createInventoryList():
    with open("./datasets/all_items.txt") as f:
        ib = f.read().splitlines()
        print len(ib)
        time.sleep(2)
        for i in ib:
            print i
            inventorylist.append(i)

def transactionlistcreator():
    with open('./datasets/groceries_cleaned.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print transaction
            print type(transaction)
            transactionlist.append(transaction)
        # print len(readCSV)

def createobjectlist():
    for inventoryItem in inventorylist:
        I = Item(inventoryItem)
        objectlist.append(I)

def writeToFile():
    thefile = open('./datasets/itemsales.txt', 'w')
    for item in objectlist:
        thefile.write(item.name+","+str(item.soldQ1)+","+str(item.soldQ2)+","+str(item.soldQ3)+"\n")

#CALL FUNCTIONS
createInventoryList()
transactionlistcreator()
createobjectlist()


print " = = = = = = OBJECTS = = = = = = ="
time.sleep(2)
for itemobject in objectlist:
    print itemobject.name
print len(inventorylist)

print "* * * * * * * * * * * * * * * * * *"

for inventoryItem in inventorylist:
    print inventoryItem

print "* * * * * * * * * * * * * * * * * *"
time.sleep(2)

for transaction in transactionlist:
    print transaction

print "* * * * * * * * * * * * * * * * * *"
time.sleep(2)

for objectx in objectlist:
    print objectx.name + " " + str(objectx.soldQ1)

print "* * * * * * * * * * * * * * * * * *"
time.sleep(2)

print "CREATING ITEM COUNTER"

for purchase in transactionlist:
    for purchasedItem in purchase:
        for obj in objectlist:
            if purchasedItem == obj.name:
                print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
                obj.soldQ1 = obj.soldQ1 + 1


time.sleep(2)
for ou in objectlist:
    print ou.name + "  = " + str(ou.soldQ1)

time.sleep(2)
print "WRITNG"
writeToFile()