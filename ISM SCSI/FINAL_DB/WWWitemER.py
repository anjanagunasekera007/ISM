import sys
import time
import csv
from WWWITEMCLASS import Item
from Sales_Calculator import returnSales


inventorylist = []
objectlist = []
def creteitemdetailist():
    with open('D:\FYP\ISM SCSI\datasets\WWWalldata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for it in readCSV:
            inventorylist.append(it)
            print(it)
            print(type(it))

def createobjectlist():
    counter = 1
    for it in inventorylist:
        print(it)
        print(type(it))
        I = Item(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],it[11],it[12],it[13])
        #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
        objectlist.append(I)
        counter = counter +1

def printobjects():
    for ob in objectlist:
        print(ob.id+" =>" + ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price + " UUU" + str(ob.soldQ1)+"+"+ str(ob.soldQ2)+ "+"+str(ob.soldQ3)+"+"+ str(ob.soldQ4) + "  TOTAL " + str(ob.soldTotal)
)

def insertSalesdata():
    h = 0
    for i in ilist:
        print str(h) + " " + i.name
        time.sleep(0.5)
        objectlist[h].soldQ1 = i.soldQ1
        objectlist[h].soldQ2 = i.soldQ2
        objectlist[h].soldQ3 = i.soldQ3
        objectlist[h].soldQ4 = i.soldQ4
        objectlist[h].soldTotal = i.soldTotal
        h = h +1


creteitemdetailist()
createobjectlist()
print " - - - - - - - "
time.sleep(2)
# printobjects()
print "- - - - - - - - -  - -"
ilist = returnSales()
g = ilist[0]
print " : : : : : : : : : : : : : : : :"
print type(g)
print str(g)
print str(len(ilist))
for i in ilist:
    print str(i.id) + " " + i.name + " " + i.description + " = = || = = " + str(i.soldQ1) + " " + str(i.soldQ2) + " TOTAL " + str(i.soldTotal)
print "DONE - - - =  - = - = - = -"
insertSalesdata()
time.sleep(2)
printobjects()
print "COMPLETED ALL OPERATIONS"