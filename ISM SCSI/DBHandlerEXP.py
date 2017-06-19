import sys
import time
import csv
import MySQLdb
from Item_Class import EXPItem
from Sales_Calculator import returnSales


from random import randint

print( "Handler initiated")
print("10")
# ilist = returnSales()
db = MySQLdb.connect("localhost","root","","ISMEXP")


cursor = db.cursor()

inventorylist = []
objectlist = []

def DeleteRecords():
    # cursor.execute("DELETE * FROM lol")
    # db.commit()
    sql = "TRUNCATE lol"
    cursor.execute(sql)
    db.commit()

DeleteRecords()
sys.exit(111)

withsaleslist = returnSales()
for item in withsaleslist:
    print type(item)
    print item.name
    print  str(item.soldQ1) + " "  + str(item.soldQ2) + " " + str(item.soldQ3) + " " + str(item.soldQ4) + "  => " + str(item.soldTotal)
    # print item.soldQ1



datelist = ["2017-7-8","2017-9-1","2017-9-18","2017-11-1","2017-11-8","2017-8-1"]
def getDate():
    print "Getting date"
    i = (randint(0, 5))
    return datelist[i]

def creteitemdetailist():
    with open('D:/FYP/ISM SCSI/datasets/alldata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for it in readCSV:
            newdate = getDate()
            it.append(newdate)
            print type(it)
            inventorylist.append(it)
            print(it)
            print(type(it))

def createobjectlist():
    counter = 0
    for it in inventorylist:
        print(it)
        print(type(it))
        I = EXPItem(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],it[11],it[12],it[13],it[14])
        #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
        I.expiredate = it[15]
        I.soldQ1 = withsaleslist[counter].soldQ1
        I.soldQ2 = withsaleslist[counter].soldQ2
        I.soldQ3 = withsaleslist[counter].soldQ3
        I.soldQ4 = withsaleslist[counter].soldQ4
        I.soldTotal = withsaleslist[counter].soldTotal
        print I.name
        print  str(I.soldQ1) + " " + str(I.soldQ2) + " " + str(I.soldQ3) + " " + str(I.soldQ4) + "  => " + str(I.soldTotal)
        objectlist.append(I)
        counter = counter +1

def insertItems():
    for ob in objectlist:
        print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
       )
        query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber,soldQ1,soldQ2,soldQ3,soldQ4,soldTotal,expiration_date)" \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (ob.name,
                ob.description,
                ob.categoryname,
                ob.category,
                ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
                ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber,ob.soldQ1,ob.soldQ2,ob.soldQ3,ob.soldQ4,ob.soldTotal,ob.expiredate)
        cursor.execute(query, args)
        db.commit()

creteitemdetailist()
createobjectlist()
insertItems()
print "SLEEPING"
time.sleep(2)
for I in objectlist:
    print  str(I.soldQ1) + " " + str(I.soldQ2) + " " + str(I.soldQ3) + " " + str(I.soldQ4) + "  => " + str(I.soldTotal) + " EXPIRES ON " + str(I.expiredate)


sys.exit(76)
#==========================================
# inventorylist = []
# objectlist = []




datelist = ["2017-7-8","2017-9-1","2017-9-18","2017-11-1","2017-11-8","2017-8-1"]
def getDate():
    print "Getting date"
    i = (randint(0, 5))
    return datelist[i]

def creteitemdetailist():
    with open('D:/FYP/ISM SCSI/datasets/alldata.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for it in readCSV:
            newdate = getDate()
            it.append(newdate)
            print type(it)
            inventorylist.append(it)
            print(it)
            print(type(it))

# olist = returnSales()
#
# for u in olist:
#     print u.name + " ... "  + str(u.soldQ1) + " " + str(u.soldQ2) + " " +str(u.soldQ3)  + "  " + str(u.soldQ4) + " = > " +str(u.soldTotal)

sys.exit(3333)
# def createobjectlist():
#     counter = 0
#     for it in inventorylist:
#         print(it)
#         print(type(it))
#         I = EXPItem(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],it[11],it[12],it[13],it[14])
#         #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
#         I.expiredate = it[15]
#         I.soldQ1 = olist[counter].soldQ1
#         I.soldQ2 = olist[counter].soldQ2
#         I.soldQ3 = olist[counter].soldQ3
#         I.soldQ4 = olist[counter].soldQ4
#         I.soltTotal = olist[counter].soldTotal
#         print str(counter) + "   " + str(I.suppliername) + " ==> " + " EXPIRES ON : " + I.expiredate
#         objectlist.append(I)
#         counter = counter +1

for finalitem in objectlist:
    print finalitem.name +  "  = >  " +  str(finalitem.soldTotal)

sys.exit(2)
# olist = returnSales()

for t in olist:
    print t.name + " " + str(t.soldTotal)
    print type(t)



print " SLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEP"
time.sleep(2)
for ob in objectlist:
    print ob.name + "  " + str(ob.soldTotal)



# sys.exit(99)

# def insertItems():
#     for ob in objectlist:
#         print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
#        )
#         query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber,soldQ1,soldQ2,soldQ3,soldQ4,soldTotal,expiration_date)" \
#                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         args = (ob.name,
#                 ob.description,
#                 ob.categoryname,
#                 ob.category,
#                 ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
#                 ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber,ob.soldQ1,ob.soldQ2,ob.soldQ3,ob.soldQ4,ob.soldTotal,ob.expiredate)
#         cursor.execute(query, args)
#         db.commit()
#==========================================


sys.exit(77)
def getallitems():
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))

    itemslist = [list(x) for x in results]
    for g in itemslist:
        print (str(type(g)))
        print g
    print (" CCCCCCCCCCCCCCCCCCCCCC")
    return itemslist

# def createObjectlist():
#     fobjlist = []
#     itemslist = getallitems()
#     for t in itemslist:
#         print t
#     print "creating list"
#     counter =1
#     for it in itemslist:
#         print it
#         I = EXPItem(counter, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10], it[11], it[12], it[13],it[19])
#         I.soldQ1 = int(it[14])
#         I.soldQ2 = int(it[15])
#         I.soldQ3 = int(it[16])
#         I.soldQ4 = int(it[17])
#         I.soldTotal = int(it[18])
#
#         counter = counter +1
#         fobjlist.append(I)
#     # time.sleep()
#
#     for rr in fobjlist:
#         print rr.name + "  "  + str(type(rr)) + "  " + str(rr.expiredate) + "   => " + str(rr.soldTotal)
    # return fobjlist
#================================================================
createObjectlist()
#===========================================================================
    # return fobjlist
# creteitemdetailist()
# createobjectlist()
# insertItems()
# print " Insertion completed "
# createObjectlist()

















# ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
# These methods are only to be used when populating the database
# inventorylist = []
# objectlist = []
#
# datelist = ["2017-7-8","2017-9-1","2017-9-18","2017-11-1","2017-11-8","2017-8-1"]
# def getDate():
#     print "Getting date"
#     i = (randint(0, 5))
#     return datelist[i]
#
# def creteitemdetailist():
#     with open('D:/FYP/ISM SCSI/datasets/alldata.csv') as csvfile:
#         readCSV = csv.reader(csvfile, delimiter=',')
#         for it in readCSV:
#             newdate = getDate()
#             it.append(newdate)
#             print type(it)
#             inventorylist.append(it)
#             print(it)
#             print(type(it))
#
# olist = returnSales()
#
#
# def createobjectlist():
#     counter = 0
#     for it in inventorylist:
#         print(it)
#         print(type(it))
#         I = EXPItem(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],it[11],it[12],it[13],it[14])
#         #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
#         I.expiredate = it[15]
#         I.soldQ1 = olist[0].soldQ1
#         I.soldQ2 = olist[0].soldQ2
#         I.soldQ3 = olist[0].soldQ3
#         I.soldQ4 = olist[0].soldQ4
#         I.soltTotal = olist[0].soldTotal
#         print str(counter) + "   " + str(I.suppliername) + " ==> " + " EXPIRES ON : " + I.expiredate
#         objectlist.append(I)
#         counter = counter +1
#
# olist = returnSales()
#
# for t in olist:
#     print t.name + " " + str(t.soldTotal)
#     print type(t)
#
#
#
# print " SLEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEP"
# time.sleep(2)
# for ob in objectlist:
#     print ob.name + "  " + str(ob.soldTotal)
#
#
#
# # sys.exit(99)
#
def insertItems():
    for ob in objectlist:
        print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
       )
        query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber,soldQ1,soldQ2,soldQ3,soldQ4,soldTotal,expiration_date)" \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (ob.name,
                ob.description,
                ob.categoryname,
                ob.category,
                ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
                ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber,ob.soldQ1,ob.soldQ2,ob.soldQ3,ob.soldQ4,ob.soldTotal,ob.expiredate)
        cursor.execute(query, args)
        db.commit()

# creteitemdetailist()
# createobjectlist()
insertItems()
print " INSERTION COMPLETED"
# ()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
