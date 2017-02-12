import csv
from Item import Item

itemnames = [];
items = []

def createItemList():
    with open("./datasets/all_items.txt") as f:
        content = f.readlines()

        for item in content:
            # print item
            itemnames.append(item)

def createObjectList():
    for name in itemnames:
        theItem = Item(str(name))
        items.append(theItem)



def loaditemsales():
    counter =0
    with open('./datasets/testdata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print ("ROW :")
            for item in row:
               print ("ITEM IN ROW " + str(item))
               for ire in items:
                   print ("Finding in all item list : " + str(ire.itemName))
                   if(str(ire.itemName) == str(item)):
                       print (" = = =  ITEM FOUND = = = ")
                       ire.sold = ire.sold+1
            counter = counter +1

def printItemList():
    for u in items:
        print (u.itemName + "  "+ str(u.sold))

createItemList()
createObjectList()
# printItemList()

loaditemsales()
printItemList()
print (" - - -")