# import csv
# import sys
# import time
# from Item_Class import  Item
#
#
# #D:\FYP\R\FINAL_CLUSTERING_SCRIPT\clusters.txt
#
# li = []
# customerlist = []
# customertransactionlist = []
# inventorylist = []
# objectlist = []
#
# c1 = []
# c1items = []
# c1soretedItems = []
#
# c2 = []
# c2items = []
# c2soretedItems = []
#
# c3 = []
# c3items  = []
# c3soretedItems = []
#
# c4 = []
# c4items = []
# c4soretedItems = []
#
# c5 = []
# c5items = []
# c5soretedItems = []
#
# c6 = []
# c6items = []
# c6soretedItems = []
#
# c7 = []
# c7items = []
# c7soretedItems = []
#
# def customerclusterreader():
#     f = open("D:\FYP\R\FINAL_CLUSTERING_SCRIPT\clusters.txt")
#     for month in f.readlines():
#         t = month.strip()
#         t = t.split(",")
#         li.append(filter(None, t))
#         print type(t)
#         print len(t)
#
#     for item in li:
#         for customer in item:
#             customerlist.append(customer)
#
#     print "=================================="
#     time.sleep(2)
#     for c in customerlist:
#         print c
#
#     print  str(len(customerlist))
#
#
# def readitemlists():
#         counter = 0
#         with open('./datasets/COMBINED_ITEMS.csv') as csvfile:
#             readCSV = csv.reader(csvfile, delimiter=',')
#             for transaction in readCSV:
#                 print filter(None, transaction)
#                 customertransactionlist.append(filter(None,transaction))
#                 print type(transaction)
#                 counter = counter + 1
#             # print str(len(readCSV))
#             print str(counter)
#
#
#
# def addclusterationtolists():
#     counter = 0
#     for i in customerlist:
#         print i + str(type(i))
#         if i == "1":
#             print "FOUND 1 " + i + " COUNTER : " + str(counter)
#             c1.append(i)
#             c1items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "2":
#             print "FOUND 2 " + i + " COUNTER : " + str(counter)
#             c2.append(i)
#             c2items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "3":
#             print "FOUND 3 " + i + " COUNTER : " + str(counter)
#             c3.append(i)
#             c3items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "4":
#             print "FOUND 4 " + i + " COUNTER : " + str(counter)
#             c4.append(i)
#             c4items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "5":
#             print "FOUND 5 " + i + " COUNTER : " + str(counter)
#             c5.append(i)
#             c5items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "6":
#             print "FOUND 6 " + i + " COUNTER : " + str(counter)
#             c6.append(i)
#             c6items.append(customertransactionlist[counter])
#             counter = counter +1
#         if i == "7":
#             print "FOUND 7 " + i + " COUNTER : " + str(counter)
#             c7.append(i)
#             c7items.append(customertransactionlist[counter])
#             counter = counter + 1
#     time.sleep(2)
#     print "THE COUNT IS : " + "    =>  " + str(counter)
#     time.sleep(2)
#
# #========================================== MERGE =====================================
# def createInventoryList():
#     with open("./datasets/all_items.txt") as f:
#         ib = f.read().splitlines()
#         print len(ib)
#         time.sleep(2)
#         for i in ib:
#             print i
#             inventorylist.append(i)
#
# def createobjectlist():
#     for inventoryItem in inventorylist:
#         I = Item(inventoryItem)
#         objectlist.append(I)
#
# def mergeSales():
#     for purchase in c1items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc1 = obj.itemc1 + 1
#
#     for purchase in c2items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc2 = obj.itemc2 + 1
#
#     for purchase in c3items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc3 = obj.itemc3 + 1
#
#     for purchase in c4items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc4 = obj.itemc4 + 1
#
#     for purchase in c5items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc5 = obj.itemc5 + 1
#
#     for purchase in c6items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc6 = obj.itemc6 + 1
#
#     for purchase in c7items:
#         for purchasedItem in purchase:
#             for obj in objectlist:
#                 if purchasedItem == obj.name:
#                     print "MATCHED " + purchasedItem + " == = = = = == " + obj.name
#                     obj.itemc7 = obj.itemc7 + 1
#
#
# def printOBJS():
#     for item in objectlist:
#         print "  " + item.name + "  " + str(item.itemc1) + " " + str(item.itemc2)+ " " + str(item.itemc3) + " " + str(item.itemc4)+ " " + str(item.itemc5) + " " + str(item.itemc6) + " " + str(item.itemc7)
#
# def sortlist():
#    # c1soretedItems =  objectlist.sort(key=lambda x: x.soldTotal, reverse=True)
#    c1soretedItems = sorted(objectlist, key=lambda x: x.itemc1, reverse=True)
#    c2soretedItems = sorted(objectlist, key=lambda x: x.itemc2, reverse=True)
#    c3soretedItems = sorted(objectlist, key=lambda x: x.itemc3, reverse=True)
#    c4soretedItems = sorted(objectlist, key=lambda x: x.itemc4, reverse=True)
#    c5soretedItems = sorted(objectlist, key=lambda x: x.itemc5, reverse=True)
#    c6soretedItems = sorted(objectlist, key=lambda x: x.itemc6, reverse=True)
#    c7soretedItems = sorted(objectlist, key=lambda x: x.itemc7, reverse=True)
#
#
# #=================================================================================================
# customerclusterreader()
# readitemlists()
#
# ui = ["1","3","5","7","9"]
# print " FIRST ELEMENT " + ui[0]
# print " SECOND ELEMENT " + ui[1]
#
# time.sleep(2)
# addclusterationtolists()
# print "added to lists"
# time.sleep(2)
#
# print str(len(customertransactionlist)) + "   " + str(len(customerlist))
# time.sleep(2)
#
# print "LENTHS "
# print  " C1 " + str(len(c1))
# print  " C2 " + str(len(c2))
# print  " C3 " + str(len(c3))
# print  " C4 " + str(len(c4))
# print  " C5 " + str(len(c5))
# print  " C6 " + str(len(c6))
# print  " C7 " + str(len(c7))
# print " TOT CUSTOMERS " + str(len(c1) + len(c2) + len(c3) + len(c4) + len(c5) + len(c6) + len(c7))
# print " TOT ITEMS " + str(len(c1items) + len(c2items) + len(c3items) + len(c4items) + len(c5items) + len(c6items) + len(c7items))
#
# print " TOT CUSTOMERS " + str(len(c1)) + " " + str(len(c2)) + " " + str(len(c3)) + " " + str(len(c4)) + " " + str(len(c5)) + " " + str(len(c6)) + " " + str(len(c7))
# print " TOT ITEMS " + str(len(c1items)) + " " + str(len(c2items)) + " " + str(len(c3items)) + " " +str(len(c4items)) + " " + str(len(c5items)) + " " + str(len(c6items)) + " " +str(len(c7items))
#
# print " CONNECTING"
# time.sleep(2)
# createInventoryList()
# createobjectlist()
# mergeSales()
# sortlist()
# printOBJS()
# print " DONE"
