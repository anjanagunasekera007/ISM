from Item_Class import Item
from D_Structure import DStructure
import time
import csv
import sys


Itemlist = []
TransactionList = []
ObjectList = []


def createInventoryList():
    with open("all_items.txt") as f:
        ib = f.read().splitlines()
        print len(ib)
        time.sleep(2)
        for i in ib:
            # print i
            Itemlist.append(i)

def createobjectlist():
    for inventoryItem in Itemlist:
        I = Item(inventoryItem)
        ObjectList.append(I)

def createTransactionList():
    with open('groceries_cleaned.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            TransactionList.append(transaction)



def ItemSales():
    for purchase in TransactionList:
        for purchasedItem in purchase:
            for obj in ObjectList:
                if purchasedItem == obj.ItemName:
                    print "MATCHED " + purchasedItem + " == = = = = == " + obj.ItemName
                    obj.count = obj.count + 1


def removeUnwanted(minSup):
    for item in ObjectList:
        print str(item.count) + "  is the count of "+ "|"+item.ItemName+"|"
        # if(item.ItemName=="UHT-milk"):
        #     sys.exit(11)
        # if(item.count < minSup):
        #     print "       Removing " + item.ItemName + " Because " + str(item.count) + " < " + str(minSup)
        #     ObjectList.remove(item)

        frequentitemlist = []



frequentitems = []




def createItemSet():
     for i in frequentitems:
          print frequentitems[168]

valid_items = []
minSup = 15
time.sleep(2)
removed = 0
print  " = = = = = =  COMPLETED  = = = = = ="


#INIT
createInventoryList()
createTransactionList()
createobjectlist()

# sys.exit(909)
ItemSales()
createItemSet()


removeUnwanted(minSup)


print "== = = = = = ==== == =  = == ="

for object in ObjectList:
    if object.count < 600:
        print "MINSUPPORT FAILED" + " - - > " + str(object.count)
    else:
        valid_items.append(object)

print " Filteration completed"

time.sleep(2)
for a in valid_items:
    print a.ItemName + "   " + " => " + str(a.count)
# removeUnwanted(minSup)

print " = = = = = * * * = = = " + str(len(valid_items))

print valid_items[1].ItemName
# def frequentitemsets():
#     print "F ITEMS"

# ******************************************* NEW *************************************** SECTION 1

Dlist = []
correct_item_sets = []

def creteitemsets():
    # counter =0
    for i in valid_items:
        counter =0
        for j in valid_items:
            DS = DStructure(i.ItemName,valid_items[counter].ItemName)
            counter = counter +1
            Dlist.append(DS)


creteitemsets()
for u in Dlist:
    print u.Item1Name + " " + u.Item2Name

for io in Dlist:
    if io.Item1Name == io.Item2Name:
        print "= FAILED "  + "   " + io.Item1Name + "  =  " + io.Item2Name
    else:
        correct_item_sets.append(io)
        print "Appended correctly"


for ui in correct_item_sets:
    print "= GOOD ITEM SET " + "   " + ui.Item1Name + "  =  " + ui.Item2Name



# ****************************************************************************************

# =============================== NEW ============================================ SECTION 2

# TransactionList
flag1 = False
flag2 = False
# for itemset in correct_item_sets:
#     print "============itemset = 1 ST FOR LOOP============================= " + str(type(itemset))
#     for transaction in TransactionList:
#         print "==================transaction = 2 ND FOR LOOP=============================" + " " + str(len(transaction))
#         for item in transaction:
#             print "=======================item n transaction 3 RD FOR LOOP===== * * * * * * * * *  " + item
#             if item == itemset.Item1Name:
#                 print " Item 1 found"
#                 flag1 = True
#             if item == itemset.Item2Name:
#                 print "     Item 2  found"
#                 flag2 = True
#             if flag1 and flag2:
#                 itemset.count = itemset.count+1
#             print "=================================================================="

for itemset in correct_item_sets:
    print "1 itemset " + itemset.Item1Name + " " + itemset.Item2Name + "  COUNT => " + str(itemset.count)
    flag1 = False
    flag2 = False
    for transaction in TransactionList:
        flag1 = False
        flag2 = False
        print transaction
        for item in transaction:
            print "======"
            print "2 ;lol  " + item
            if item == itemset.Item1Name:
                flag1 = True
                print "3  MATCHED " + item + " = " + itemset.Item1Name + " +++ " + str(flag1)
            if item == itemset.Item2Name:
                flag2 = True
                print "3  MATCHED " + item + " = " + itemset.Item2Name + " +++ " + str(flag2)
            if flag1 and flag2:
                print " IF Flag 1 " + str(flag1) + "  - - " + "Flag 2" + str(flag2) + " MATCHES"
                itemset.count = itemset.count+1
                flag1 = False
                flag2 = False
            print "=================================================================="



print " 00000000000000000000  ANALYZATION COMPLETED 0000000000000000000000000000"
time.sleep(2)

for k in correct_item_sets:
    print "= GOOD ITEM SET " + "   " + k.Item1Name + "  =  " + k.Item2Name + " === > " + str(k.count)


#===================================================================================




