import MySQLdb
import csv
# from NNNITEMCLASS import Item
# from NNNITEMCLASS import Item
from Item_Class import uItem
from Sales_Calculator import returnSales
import time
import sys
import datetime
from Notification_Class import ReStockNotification
from Notification_Class import  ReOrderNotification
# from Notification_Class import ReStockNotification

print( "Handler initiated")
print("10")
# ilist = returnSales()
db = MySQLdb.connect("localhost","root","","ISM")

#cursor object
cursor = db.cursor()

# cursor.execute("SELECT VERSION()")

# data = cursor.fetchone()

# print "Database version : %s " % data

# db.close()

def createTables():
    sql  = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

    cursor.execute(sql)

def insertData():
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

    user_id = "test123"
    password = "password"

    # cursor.execute('insert into EMPLOYEE values("%s", "%s")',  % \
    #             (user_id, password))

    query = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)"  \
                          "VALUES(%s,%s,%i,%c,%f)"
    args = ("Fname","lname",23,"M",19.96)

    cursor.execute(query,args)
    #
    # try:
    #     # Execute the SQL command
    #     cursor.execute(sql)
    #     # Commit your changes in the database
    #     db.commit()
    # except:
    #     # Rollback in case there is any error
    #     db.rollback()
    #
    #     # db.close()

# =========================================================================================
inventorylist = []
objectlist = []
def creteitemdetailist():
    with open('D:/FYP/ISM SCSI/datasets/alldata.csv') as csvfile:
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
        I = uItem(it[0], it[1], it[2],it[3],it[4],it[5],it[6],it[7],it[8],it[9],it[10],it[11],it[12],it[13])
        #              id,   name, description, categoryname, category, instock, inshelf, minorder, price, weight):
        objectlist.append(I)
        counter = counter +1

def printobjects():
    for ob in finalobjectlist:
        print(ob.id+" =>" + ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price + " UUU" + str(ob.soldQ1)+"+"+ str(ob.soldQ2)+ "+"+str(ob.soldQ3)+"+"+ str(ob.soldQ4) + "  TOTAL " + str(ob.soldTotal)
)

# def insertItems():
#     for ob in objectlist:
#         print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
#        )
#         query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber)" \
#                 "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         args = (ob.name,
#                 ob.description,
#                 ob.categoryname,
#                 ob.category,
#                 ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
#                 ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber)
#         cursor.execute(query, args)
#         db.commit()

def insertItems():
    for ob in objectlist:
        print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
       )
        query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber,soldQ1,soldQ2,soldQ3,soldQ4,soldTotal)" \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (ob.name,
                ob.description,
                ob.categoryname,
                ob.category,
                ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
                ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber,ob.soldQ1,ob.soldQ2,ob.soldQ3,ob.soldQ4,ob.soldTotal)
        cursor.execute(query, args)
        db.commit()

def createItemlist():
    salesitemlist = returnSales()
    return salesitemlist

# ==================================================  RETRIEVE DATA
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


def getAllRestockNotifications():
    notificationreturnslist = []
    sql = "SELECT * FROM restock"
    cursor.execute(sql)
    results = cursor.fetchall()
    print "ALL NOTIFICATIONS RESTOCK"
    for t in results:
        print (str(t[0]) + " " + t[1])
        print str(type(t[0])) + " " + str(type(t[1])) + " " + str(type(t[2])) + " " + str(type(t[3])) + " " + str(type(t[4]))
        print len(t)
        rn = ReStockNotification(str(t[0]),t[1],t[2],str(t[3]),str(t[3]),t[4])
        notificationreturnslist.append(rn)
    return  notificationreturnslist


def getAllReorderNotifications():
    notificationreturnslist = []
    sql = "SELECT * FROM reorder"
    cursor.execute(sql)
    results = cursor.fetchall()
    print "ALL NOTIFICATIONS REORDER"
    for t in results:
        print (str(t[0]) + " " + t[1])
        print str(type(t[0])) + " " + str(type(t[1])) + " " + str(type(t[2])) + " " + str(type(t[3])) + " " + str(
            type(t[4]))
        print len(t)
        rn = ReOrderNotification(str(t[0]), t[1], t[2], str(t[3]), t[5])
        notificationreturnslist.append(rn)
    return notificationreturnslist







    # itemslist = [list(x) for x in results]
    # for g in itemslist:
    #     print (str(type(g)))
    #     print g
    # print (" CCCCCCCCCCCCCCCCCCCCCC")
    # return itemslist

def updateitem():
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET instock = instock - %s WHERE itemname = %s",
                (20, "UHT-milk"))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

def updateShelf(count,itemname):
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET inshelf =  %s WHERE itemname = %s",
                (count, itemname))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

def updateStock(count,itemname):
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET inshelf =  %s WHERE itemname = %s",
                (count, itemname))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

# def insertSalesdata():
#     h = 0
#     for i in ilist:
#         print str(h) + " " + i.name
#         time.sleep(0.5)
#         objectlist[h].soldQ1 = i.soldQ1
#         objectlist[h].soldQ2 = i.soldQ2
#         objectlist[h].soldQ3 = i.soldQ3
#         objectlist[h].soldQ4 = i.soldQ4
#         objectlist[h].soldTotal = i.soldTotal
#         h = h +1

# def databaseObjList():
finalobjectlist = []
dblist = []
def crObjfromDB():
    print "creating list"
    counter =1
    for it in dblist:
        print it
        I = uItem(counter, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10], it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        counter = counter +1
        finalobjectlist.append(I)

sourcelist = []
flist = []
def returnflist():
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))
        sourcelist.append(t)
    print "creating list"
    counter =1
    for it in sourcelist:
        print it
        I = uItem(counter, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10], it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        counter = counter +1
        flist.append(I)
    return flist


def getitemscreateobj():
    fobjlist = []
    itemslist = getallitems()
    for t in itemslist:
        print t
    print "creating list"
    counter =1
    for it in itemslist:
        print it
        I = uItem(counter, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10], it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        counter = counter +1
        fobjlist.append(I)
    return fobjlist
def returnobjs():
    print ("EXECUTIONS")
    creteitemdetailist()
    createobjectlist()

    # insertSalesdata()
    print " INSERTED ALL ITEMS"
    getallitems()
    dblist = getallitems()
    print " u u u u u u u u"
    print "YAWOOOOOOOOOOOO"
    print "CREATING OBJECT LIST YOOOOOO"
    crObjfromDB()
    print str(len(finalobjectlist))
    sys.exit(888)
    for y in finalobjectlist:
        print str(y.id) + " " + y.name + " " + str(y.soldTotal)
    print "FINALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
    print "COMPLETED ALL OPERATIONS"

# punklist = getitemscreateobj()
# print str(len(punklist))
# # sys.exit(9876)
# for t in punklist:
#     print t.name + " " + t.description + "  = = " + str(t.soldTotal)
# print "C O M P L E T E D - * - *- +*- +*- -+ *- +-* + *- + *- +*- 9* - *- * * + *-"

# ================================================
def storeRestockNotification(notification,qty,status):
    print "storing notification for restock"
    query = "INSERT INTO restock(notification,itemqty, status)" \
            "VALUES(%s,%s,%s)"
    args = (notification,
            qty,
            status,
            )
    cursor.execute(query, args)
    db.commit()

def storeReorderNotification(notification,qty,status):
    print "storing notification for reorder"
    ts = datetime.datetime.now()
    end_date = ts + datetime.timedelta(days=7)
    edate = str(end_date)
    query = "INSERT INTO reorder(notification,itemqty, status,deliverydate)" \
            "VALUES(%s,%s,%s,%s)"
    args = (notification,
            qty,
            status,
            edate,
            )
    cursor.execute(query, args)
    db.commit()



def getReorderNotification():
    v = cursor.lastrowid
    sql = "SELECT * FROM reorder \
           WHERE id = '%s'" % (v)
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))

def getRestockNotification():
    v = cursor.lastrowid
    sql = "SELECT * FROM restock \
           WHERE id = '%s'" % (v)
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))


# storeRestockNotification("restockthis please","50","NOTIFIED")
# storeReorderNotification("tytytyty","60","NOTIFIED")
# v = cursor.lastrowid
# print (v)
# getReorderNotification()


#=======================================================================================================================================
#=======================================================================================================================================
#=======================================================================================================================================

# $The pos function updates the records with a new number to emulate item transations
#the amount that is substracted can change from time to time
#hence it is called manually and fixed


DBItemList = []
OBJECTSLIST = []
OBJECTSLIST2 = []
runningout = []
stockdepleting = []
#=========================================================================
def updateSTOCK(qty,name):
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET instock = instock - %s WHERE itemname = %s",
                (qty, name))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

def updateSHELF_POS(name):
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET inshelf = inshelf - %s WHERE itemname = %s",
                (5, name))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()


def CreateItemlistfromDBRESTOCK():
    DBItemlist = []
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))
        DBItemlist.append(t)

    idd= 1
    for it in DBItemlist:
        print it
        I = uItem(idd, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10],
                      it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        idd = idd + 1
        OBJECTSLIST.append(I)

    for nb in OBJECTSLIST:
        if nb.inshelf <= 5:
            print "ITEM FOUND : --->  " + nb.name
            runningout.append(nb)

def CreateItemListfromDBREORDER():
    print "CREATING : : : : "
    time.sleep(2)
    DBItemlist = []
    sql = "SELECT * FROM items"
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))
        DBItemlist.append(t)

    idd= 1
    for it in DBItemlist:
        print it
        I = uItem(idd, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10],
                      it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        idd = idd + 1
        OBJECTSLIST2.append(I)

    for ro in OBJECTSLIST2:
        if ro.instock <=150:
            print " ITEM FOUND FOR REORDER  -->" + ro.name
            stockdepleting.append(ro)


restocknotifications = []
def creteNotificationsRESTOCK():
    for item in runningout:
        qty = item.shelfcapacity - item.inshelf

        n = ReStockNotification("0",item.name,qty,time.strftime("%d/%m/%Y"),time.strftime("%d/%m/%Y"),"Pending")
        restocknotifications.append(n)
        storeRestockNotification(n.notification, qty, n.status)
        print "NOTIFICATION CREATED AND STORED"
        print n.notification
        print n.ITEMQty
        print "\n"

    print "ALL NOTIFICATIONS HAVE BEEN STORED"


reordernotifications = []
def createNotificationsREORDER():
    print " CREATING NOTIFICATIONS FOR RESORDER DB "
    time.sleep(2)
    for item in stockdepleting:
        qty = 400

        n = ReOrderNotification("0",item.name,qty,time.strftime("%d/%m/%Y"),"Pending")
        restocknotifications.append(n)
        storeReorderNotification(n.notification, qty, n.status)
        print "NOTIFICATION CREATED AND STORED FOR STOCKS DEPLETING"
        print n.notification
        print n.ITEMQty
        print "\n"

    print "ALL NOTIFICATIONS HAVE BEEN STORED"


    # itemslist = [list(x) for x in results]
    # for g in itemslist:
    #     print (str(type(g)))
    #     print g
    # print (" CCCCCCCCCCCCCCCCCCCCCC")
    # return itemslist

print "===================== BEGINING EXECUTION =========================="
time.sleep(2)
# CreateItemlistfromDB()
#
# haa = 1
# for y in OBJECTSLIST:
#     print y.name + "  " +  str(haa)
#     haa = haa +1

# def getData():
#     CreateItemlistfromDB()
#     return OBJECTSLIST

# updateSTOCK(10,"UHT-milk")
def POS():
    print "Buying items"
    updateSHELF_POS("UHT-milk")
    updateSHELF_POS("baby food")
    updateSHELF_POS("bathroom cleaner")
    updateSHELF_POS("bottled beer")
    updateSHELF_POS("beverages")
    updateSHELF_POS("cooking chocolate")
    updateSHELF_POS("curd")
    updateSHELF_POS("frozen fish")
    updateSHELF_POS("liquor")
    updateSHELF_POS("long life bakery product")
    updateSHELF_POS("mustard")
    updateSHELF_POS("ice cream")

def STOCKDEPETER():
    print "ORDERING ITEMS"
    # updateSTOCK(192,"Instant food products")
    updateSTOCK(200,"bags")
    updateSTOCK(250,"cake bar")
    updateSTOCK(200,"canned beer")
    updateSTOCK(200,"canned fish")
    updateSTOCK(100,"curd cheese")
    updateSTOCK(280, "frozen meals")

    # updateSTOCK(400,"herbs")
    # updateSTOCK(400,"liqueur")
    # updateSTOCK(450, "softener")


def overallExecution():
    print " EXEXEXEXEXEEXE$XEXEXEXEXEXEXEX#$XEXEXEXEXEXEXE"
    STOCKDEPETER()
    CreateItemListfromDBREORDER()
    createNotificationsREORDER()

print " EXEC ==================================  > > > > > > "
# time.sleep(2)

# getAllRestockNotifications()
#
# s = getAllReorderNotifications()
# print type(s)
# print len(s)
# sys.exit(9999)
print("-----------------------------")
# POS()
# CreateItemlistfromDB()

# for u in runningout:
#     print u.name + "  is runing out RESTOCK"
#     print u.inshelf
#     print u.shelfcapacity
#     print " REORDER : " + str(u.shelfcapacity - u.inshelf)
#     print "\n"

# print " GENERATING NOTIFICATION"
# time.sleep(2)
# creteNotifications()
# POS()

def updateReOrderStatus(name,status):
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE reorder SET status = %s WHERE notification = %s",
                (status, name))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()