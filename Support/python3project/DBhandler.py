import
import csv
from ITEMCLASS import Item
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
    for ob in objectlist:
        print(ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
)
def insertItems():
    for ob in objectlist:
        print (ob.name + " " + ob.description + " " + ob.category + " " + ob.instock + " " + ob.inshelf + " " + ob.shelfcapacity + " " + ob.weight + " " + ob.price
       )
        query = "INSERT INTO items(itemname,description, categoryname, categoryid, price,instock,inshelf,shelfcapacity,weight,url,suppliername,supplieraddress,suppliercontactnumber)" \
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (ob.name,
                ob.description,
                ob.categoryname,
                ob.category,
                ob.price, ob.instock, ob.inshelf, ob.shelfcapacity, ob.weight,
                ob.url, ob.suppliername, ob.supplieraddress, ob.suppliercontactnumber)
        cursor.execute(query, args)
        db.commit()
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
    print (" CCCCCCCCCCCCCCCCCCCCCC")

def updateitem():
    # sql = "UPDATE items SET instock = instock - "+ "%s" + "WHERE itemname = '%s'"
    cursor.execute("UPDATE items SET instock = instock - %s WHERE itemname = %s",
                (20, "UHT-milk"))
    # args = (20,"UHT-milk")
    # cursor.execute(sql)
    db.commit()

print ("EXECUTIONS")
# createTables()
# creteitemdetailist()
# createobjectlist()
print ("----")
printobjects()
print ("-------------------")
time.sleep(2)
print (" STARTING TO PUT ITEMS")
# insertItems()
# time.sleep(2)
# print "*******************************   ***********************   ***     * * ** ** **  * * ** *** ** "
# for y in objectlist:
#     print y.name + " " + y.description + " => " + y.url
# print " run "
# insertItems()
# print "completed "
getallitems()
updateitem()
