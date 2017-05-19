# from Item_Class import FullItem
from flask import Flask , render_template ,json ,request
# from Sales_Calculator import returnSales
# from Sales_Calculator import sortlist
# from Sales_Calculator import retunleastsold
from Association_Class import Association
from DBHandler import getitemscreateobj
# from DBHandler import updatesales
import time
import sys
import json
from ARProcessor import returnAssociations
from Initialization import initiateStartup
from flask import  jsonify
from ParameterizedOperations import readImpact
from ParameterizedOperations import Impact_overall
from DBHandler import getAllRestockNotifications
from DBHandler import getAllReorderNotifications
# from AR_Reader import ARProcessor as arp
# import request
# import urllib2.request

restocks = getAllRestockNotifications()
for t in restocks:
    print t.notification + " " + str(type(t))
# sys.exit(666)
pppp = readImpact()
for y in pppp:
    print y.name
    print y.impactSize
print len(pppp)
# sys.exit(89)
status = initiateStartup()
for g in status:
    print g

# sys.exit(999)
punklist = getitemscreateobj()

print str(len(punklist))
# sys.exit(9876)
for t in punklist:
    print t.name + " " + t.description + "  = = " + str(t.soldTotal)
print "C O M P L E T E D - * - *- +*- +*- -+ *- +-* + *- + *- +*- 9* - *- * * + *-"
time.sleep(3)
AssociationsList = returnAssociations()
for t in AssociationsList:
    print t.rule
    print type(t.rule)
# sys.exit(678)

app = Flask(__name__)
app.config['DEBUG'] = True

#EXTERNAL FUNCTIONS
#
# ty = arp.returnAssociations()
# print (len(ty))
# sys.exit(88)

#*************************************************************
# ItemList = returnSales()
print "================"
print str(type(punklist[0]))
print (punklist[0])
print (punklist[0])
print punklist[0].name
print punklist[0].description
print ";;;;;;;;"
y = punklist[0]
print type(y)
print y.name
print y.description

print " @@@@@@@@@@@@@@@@@@@@@@@@ "
time.sleep(2)
for g in punklist:
    print g
time.sleep(2)
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
# sys.exit(6969)
print "===================== 0 0 0 0 0==============="
# sys.exit(889)
# newlist = sortlist()


#==================================
def sortlist(nl):
    newlist = sorted(nl, key=lambda x: x.soldTotal, reverse=True)
    for j in newlist:
        print type(newlist)
        print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
    return newlist
#==================================
from DBHandler import returnflist
newobjlist = returnflist()
newlist = sortlist(newobjlist)
# print str(len(newlist))
# print " hoooooo "
# time.sleep(2)
most = newlist[0:5]
least = newlist[164:]

print len(newobjlist)
print len(most)
print len(least)
# sys.exit(8888)
# sys.exit(87)
print "--------------------------------------------------------------- 8 8 8 ---------------------------------------"


def printem(usernamee, passwordd):
    print usernamee
    print passwordd

print ("  6969696969696969696969696969696969 ")
print str(len(punklist))

for i in punklist:
    print i.name
    print type(i)
print ("  6969696969696969696969696969696969 888")
print str(len(least))
print str(len(most))
time.sleep(2)
for j in least:
    print j.name + " TOTAL SALES :" + str(j.soldTotal)
print " k j k j k j k j k jk j j jk k j k"
# for y in punklist:
#     print y.soldQ1
#     print y.soldQ2
#     print y.soldQ3
#     print y.soldQ4
#     print y.soldTotal

counter  =0
zerolist = []
for i in least:
    if i.soldTotal ==0:
        print "FOUND"
        counter = counter +1
        zerolist.append(i)

print counter
print len(zerolist)

salesloadcounter = 0

# ===========================
from delClass import uItem
counter =0
name = ["proudct1","product2","product3"]
objarray = []
for n in name:
    obj = uItem(counter,n)
    r = json.dumps(obj.__dict__)
    counter = counter +1
    objarray.append(r)


# @app.route('/', methods=['GET', 'POST'])
# def main():
#     return render_template('ajaxjquery.html',dlist=objarray)


@app.route('/', methods=['GET', 'POST'])
def main():
    # mylist = [1,2,3,4,5,6];
    print " AIYOOOOOOOOOOO   " + str(len(zerolist))
    for item in zerolist:
        print item.name
        print item.description
    ylist = [1,2,3,4,5,6,7]
    return render_template('index.html',name="the name",mostlist=most,leastlist=least)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    mylist = [1,2,3,4,5,6];
    return render_template('dashboard.html', data = mylist,name="the name",mostlist=most,leastlist=least,zlist=zerolist )

# @app.route('/', methods=['GET', 'POST'])
# def main():
#     mylist = [1,2,3,4,5,6];
#     return render_template('dashboard.html', data = mylist,name="the name",mostlist=most,leastlist=least )
# salesloadcounter = 0
@app.route('/login', methods=['GET',  'POST'])
def login():
    error = None;
    listx  = [2,4,6,8,10]
    saleslist = punklist
    # salesloadcounter = 1
    # if salesloadcounter >=0:
    #     print "sales loader " + str(salesloadcounter)
    #     salesloadcounter = salesloadcounter +1
    #     saleslist = getitemscreateobj()
    return render_template('item_sales.html', error=error,datalist=saleslist)


@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('dashboard.html', error=error,datalist=punklist,mostlist=most,leastlist=least)

minstock = 300
# =============================================== ITEMS =========================================================================?
y = punklist[0]
@app.route('/Instantfoodproducts', methods=['GET', 'POST'])
def Instantfoodproducts():
    error = None;
    return render_template('itemwisesales.html', error=error,item=punklist[0],minstock=minstock)

@app.route('/UHTmilk', methods=['GET', 'POST'])
def UHTmilk():
    error = None;
    return render_template('ajaxjquery.html', error=error,datalist=punklist,mostlist=most,leastlist=least)

@app.route('/abrasivecleaner', methods=['GET', 'POST'])
def abrasivecleaner():
    error = None;
    return render_template('itemwisesales.html', error=error,item=punklist[2],minstock=minstock)


# =============================================== ITEMS =========================================================================?

@app.route('/signUpUser', methods=['GET','POST'])
def signUpUser():
    print "WORKING = = = =  * * FUCKKKK"
    # user = request.form['username']
    # password = request.form['password']
    # pis = " yu gi oh"
    # printem(user,password)
    # return json.dumps({'status':'OK','user':user,'pass':password,'pi':pis});
    t = jsonify(objarray)
    print t
    return t



@app.route('/itemPatterns', methods=['GET', 'POST'])
def itemPatterns():
    print "WORKING = = = =  * * FUCKKKK"
    error = None;
    # user = request.form['username']
    # password = request.form['password']
    # pis = " yu gi oh"
    # printem(user,password)
    # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
    return render_template('itempatterns.html', error=error,datalist=AssociationsList)


@app.route('/stat', methods=['GET', 'POST'])
def stat():
    print "WORKING = = = =  * * FUCKKKK"
    error = None;
    keys = request.args.get('itemname')
    print keys
    # user = request.form['username']
    # password = request.form['password']
    # pis = " yu gi oh"
    # printem(user,password)
    # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
    return render_template('itempatterns.html', error=error,datalist=AssociationsList)

@app.route('/StockNotification', methods=['GET', 'POST'])
def StockNotification():
    print "WORKING"
    error = None;
    keys = request.args.get('itemname')
    restockNotifications = getAllRestockNotifications()
    for k in restockNotifications:
        print k,status
    reorderNotifications = getAllReorderNotifications()
    print keys
    # user = request.form['username']
    # password = request.form['password']
    # pis = " yu gi oh"
    # printem(user,password)
    # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
    return render_template('stocks.html', error=error,restock=restockNotifications,reorder=reorderNotifications)


from DBHandler import updateReOrderStatus
@app.route('/createOrder', methods=['GET', 'POST'])
def createOrder():
    reorderNotifications = getAllReorderNotifications()
    itemname = request.form['itemname'] + " = = = = = =  awwooooooo"
    print itemname
    updateReOrderStatus("Instant food products", "On order")
    error = None;
    # password = request.form['password']
    # pis = " yu gi oh"
    # printem(user,password)
    # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
    return 0;

# ---------------------------------------------
from mergecomp import returnSegments
from mergecomp import returnFREQUENTITEMS
segments = returnSegments()
print len(segments)

patterns = returnFREQUENTITEMS()
# print len(patterns)
# sys.exit(456)


@app.route('/customersegments', methods=['GET', 'POST'])
def customersegments():
    # print "WORKING"
    # error = None;
    # keys = request.args.get('itemname')
    # restockNotifications = getAllRestockNotifications()
    # reorderNotifications = getAllReorderNotifications()
    # print keys
    # # user = request.form['username']
    # # password = request.form['password']
    # # pis = " yu gi oh"
    # # printem(user,password)
    # # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
    return render_template('customersegments.html')


# @app.route('/ShelfNotification', methods=['GET', 'POST'])
# def ShelfNotification():
#     print "WORKING"
#     error = None;
#     # keys = request.args.get('itemname')
#     # print keys
#     # user = request.form['username']
#     # password = request.form['password']
#     # pis = " yu gi oh"
#     # printem(user,password)
#     # return render_template('tables.html', error=error, datalist=punklist, mostlist=most, leastlist=least)
#     return render_template('shelf.html', error=error,datalist=punklist,mostlist=most,leastlist=least)

#************************ BUY ITEM **************************************
@app.route('/buyitem', methods=['POST'])
def buyitem():
    # print "WORKING = = = =  * * FUCKKKK"
    # # user = request.form['name']
    # itemid = request.form['name']
    # itemshelfcount = request.form['inshelf']
    # newcount = int(itemshelfcount) - 1
    # print "SENDING UPDATE"
    # updatesales(newcount,itemid)
    # print "COMPLETED UPDATE"
    # # itemshelfcount = int(itemshelfcount) - 1
    # # password = request.form['password']
    # print itemid
    # pis = " yu gi oh hohohohooo"
    # printem(itemid,itemshelfcount)
    # # print str(type(itemid))
    # # print str(type(itemshelfcount))
    # print " YAWOOOOZZZAAAAAA"
    # time.sleep(2)
    # # return json.dumps({'status':'OK','user':itemid,'pass':itemshelfcount,'pi':pis});
    #
    return 0;


@app.route('/getItemList', methods=['GET','POST'])
def getItemList():
    print "WORKING = = = =  * * FUCKKKK"
    u = punklist
    oblist = []
    for n in punklist:
        r = json.dumps(n.__dict__)
        oblist.append(r)
    # t = jsonify(u)
    # print t
    # for i in oblist:
    #     print i
    t = jsonify(oblist)
    return t

@app.route('/getImpactIFP', methods=['GET','POST'])
def getImpactIFP():
    print "WORKING = = = =  * * FUCKKKK"
    u = punklist
    oblist = []
    for n in pppp:
        r = json.dumps(n.__dict__)
        oblist.append(r)
    # t = jsonify(u)
    # print t
    # for i in oblist:
    #     print i
    t = jsonify(oblist)
    return t

from DBHandler import POS
from DBHandler import  CreateItemlistfromDBRESTOCK
from DBHandler import creteNotificationsRESTOCK
@app.route('/initiatePOS', methods=['GET','POST'])
def initiatePOS():
    POS()
    CreateItemlistfromDBRESTOCK()
    creteNotificationsRESTOCK()
    print "WORKING = = = =  * * FUCKKKK"
    u = punklist
    oblist = []
    for n in pppp:
        r = json.dumps(n.__dict__)
        oblist.append(r)
    # t = jsonify(u)
    # print t
    # for i in oblist:
    #     print i
    t = jsonify(oblist)
    return t

from DBHandler import STOCKDEPETER
from DBHandler import CreateItemListfromDBREORDER
from DBHandler import createNotificationsREORDER
from DBHandler import overallExecution
@app.route('/initiateDEPLETION', methods=['GET','POST'])
def initiateDEPLETION():
    print " * * * - - - * * * "
    STOCKDEPETER()
    CreateItemListfromDBREORDER()
    createNotificationsREORDER()
    print "WORKING = = = =  * * REORDER : : "
    u = punklist
    oblist = []
    for n in pppp:
        r = json.dumps(n.__dict__)
        oblist.append(r)
    # t = jsonify(u)
    # print t
    # for i in oblist:
    #     print i
    t = jsonify(oblist)
    return t


from  mergecomp import returnSegments
segmentlist = returnSegments()
@app.route('/getSegments', methods=['GET','POST'])
def getSegments():
    print " * * * - - - * * * "

    for i in segmentlist:
        print i
    # sys.exit(777)
    # STOCKDEPETER()
    # CreateItemListfromDBREORDER()
    # createNotificationsREORDER()
    # print "WORKING = = = =  * * REORDER : : "
    u = punklist
    oblist = []
    for n in segmentlist:
        r = json.dumps(n.__dict__)
        oblist.append(r)
    # t = jsonify(u)
    # print t
    # for i in oblist:
    #     print i
    t = jsonify(oblist)
    return t


#========================= EXTERNAL FUNCTIONS =======================
def sortlist(nl):
    newlist = sorted(nl, key=lambda x: x.soldTotal, reverse=True)
    for j in newlist:
        print type(newlist)
        print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
    return newlist

if __name__ == '__main__':
    app.run(debug=True)






