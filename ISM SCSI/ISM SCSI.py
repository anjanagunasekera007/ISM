# from Item_Class import FullItem
from flask import Flask , render_template ,json ,request
# from Sales_Calculator import returnSales
from Sales_Calculator import sortlist
# from Sales_Calculator import retunleastsold
from Association_Class import Association
from DBHandler import getitemscreateobj
from DBHandler import updatesales
import time
import sys
import json
from ARProcessor import returnAssociations

# from AR_Reader import ARProcessor as arp
# import request
# import urllib2.request

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
newlist = sortlist()
# print str(len(newlist))
# print " hoooooo "
# time.sleep(2)
most = newlist[0:5]
least = newlist[164:]
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

@app.route('/', methods=['GET', 'POST'])
def main():
    mylist = [1,2,3,4,5,6];
    return render_template('index.html', data = mylist,name="the name",mostlist=most,leastlist=least )

@app.route('/login', methods=['GET',  'POST'])
def login():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('item_sales.html', error=error,datalist=punklist)


@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('index.html', error=error,datalist=punklist,mostlist=most,leastlist=least)

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

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    print "WORKING = = = =  * * FUCKKKK"
    user = request.form['username']
    password = request.form['password']
    pis = " yu gi oh"
    printem(user,password)
    return json.dumps({'status':'OK','user':user,'pass':password,'pi':pis});

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


#************************ BUY ITEM **************************************
@app.route('/buyitem', methods=['POST'])
def buyitem():
    print "WORKING = = = =  * * FUCKKKK"
    # user = request.form['name']
    itemid = request.form['name']
    itemshelfcount = request.form['inshelf']
    newcount = int(itemshelfcount) - 1
    print "SENDING UPDATE"
    updatesales(newcount,itemid)
    print "COMPLETED UPDATE"
    # itemshelfcount = int(itemshelfcount) - 1
    # password = request.form['password']
    print itemid
    pis = " yu gi oh hohohohooo"
    printem(itemid,itemshelfcount)
    # print str(type(itemid))
    # print str(type(itemshelfcount))
    print " YAWOOOOZZZAAAAAA"
    time.sleep(2)
    # return json.dumps({'status':'OK','user':itemid,'pass':itemshelfcount,'pi':pis});
    return json.dumps({'user':newcount});


if __name__ == '__main__':
    app.run(debug=True)






