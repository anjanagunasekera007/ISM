import MySQLdb
import csv
from ITEMCLASS import Item
from ITEMCLASS import Item
from Sales_Calculator import returnSales
import time

print( "Handler initiated")
print("10")

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
    with open('alldata.csv') as csvfile:
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

def updateitem():
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET instock = instock - %s WHERE itemname = %s",
                (20, "UHT-milk"))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

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

# def databaseObjList():
finalobjectlist = []
def crObjfromDB():
    print "creating list"
    counter =1
    for it in dblist:
        print it
        I = Item(counter, it[1], it[2], it[3], it[4], it[5], int(it[6]), int(it[7]), int(it[8]), it[9], it[10], it[11], it[12], it[13])
        I.soldQ1 = int(it[14])
        I.soldQ2 = int(it[15])
        I.soldQ3 = int(it[16])
        I.soldQ4 = int(it[17])
        I.soldTotal = int(it[18])
        counter = counter +1
        finalobjectlist.append(I)


print ("EXECUTIONS")
# createTables()
creteitemdetailist()
createobjectlist()
print ("----")
print ("-------------------")
time.sleep(2)
print (" STARTING TO PUT ITEMS")


#****************************************************************************************************
# getallitems()
# updateitem()
#****************************************************************************************************

ilist = returnSales()
g = ilist[0]
insertSalesdata()


#****************************************************************************************************
# insertItems()
print " INSERTED ALL ITEMS"
#****************************************************************************************************
time.sleep(3)
getallitems()
dblist = getallitems()
for g in dblist:
    print g
    print "--------------------------------------------"
    print g[0]
    print int(g[0])
    # print str(type(g[0])) + " ; ; ; " + g[0]
    print "--------------------------------------------"
time.sleep(2)
print " u u u u u u u u"
print "YAWOOOOOOOOOOOO"
time.sleep(2)
time.sleep(2)
print "CREATING OBJECT LIST YOOOOOO"
crObjfromDB()
# printobjects()
for y in finalobjectlist:
    print str(y.id) + " " + y.name + " " + str(y.soldTotal)
print "FINALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
print "COMPLETED ALL OPERATIONS"