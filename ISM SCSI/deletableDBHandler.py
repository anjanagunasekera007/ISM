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

print( "Handler initiated")
print("10")
# ilist = returnSales()
db = MySQLdb.connect("localhost","root","","ISM")

#cursor object
cursor = db.cursor()

# def storeRestockNotification(notification,qty,status):
#     print "storing notification for restock"
#     query = "INSERT INTO restock(notification,itemqty, status)" \
#             "VALUES(%s,%s,%s)"
#     args = (notification,
#             qty,
#             status,
#             )
#     cursor.execute(query, args)
#     db.commit()
#     notification = getRestockNotification()
#     print notification

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
    notification = getReorderNotification()
    print len(notification)
    print (type(notification))
    print notification[0]
    print notification[1]
    print notification[2]
    print notification[3]
    print notification[4]
    print notification[5]



def getReorderNotification():
    v = cursor.lastrowid
    sql = "SELECT * FROM reorder \
           WHERE id = '%s'" % (v)
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))
    return t

def getRestockNotification():
    v = cursor.lastrowid
    sql = "SELECT * FROM restock \
           WHERE id = '%s'" % (v)
    cursor.execute(sql)
    results = cursor.fetchall()
    for t in results:
        print (str(t[0]) + " " + t[1])
        print (type(t))
    return t


# storeRestockNotification("restockthis please","50","NOTIFIED")
storeReorderNotification("ahahahahaaww","60","NOTIFIED")
v = cursor.lastrowid
print (v)
# getReorderNotification()