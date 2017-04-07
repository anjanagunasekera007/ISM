from Item_Class import FullItem
from flask import Flask , render_template ,json ,request
from Sales_Calculator import returnSales
from Sales_Calculator import sortlist
# from Sales_Calculator import retunleastsold
from DBHandler import getitemscreateobj
import time
import sys
import json
# import request
# import urllib2.request

# punklist = getitemscreateobj()
# print str(len(punklist))
# # sys.exit(9876)
# for t in punklist:
#     print t.name + " " + t.description + "  = = " + str(t.soldTotal)
# print "C O M P L E T E D - * - *- +*- +*- -+ *- +-* + *- + *- +*- 9* - *- * * + *-"
# sys.exit(678)

app = Flask(__name__)
app.config['DEBUG'] = True

#EXTERNAL FUNCTIONS



#*************************************************************
ItemList = returnSales()
print "================"
print str(type(ItemList[0]))
print (ItemList[0])
print (ItemList[0])
print ItemList[0].name
print ItemList[0].description
print ";;;;;;;;"
y = ItemList[0]
print type(y)
print y.name
print y.description

print " @@@@@@@@@@@@@@@@@@@@@@@@ "
time.sleep(2)
for g in ItemList:
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
print str(len(ItemList))

for i in ItemList:
    print i.name
    print type(i)
print ("  6969696969696969696969696969696969 888")
print str(len(least))
print str(len(most))
time.sleep(2)
for j in least:
    print j.name + " TOTAL SALES :" + str(j.soldTotal)


@app.route('/', methods=['GET', 'POST'])
def main():
    mylist = [1,2,3,4,5,6];
    return render_template('index.html', data = mylist,name="the name",mostlist=most,leastlist=least )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('item_sales.html', error=error,datalist=ItemList)


@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None;
    listx  = [2,4,6,8,10]
    return render_template('index.html', error=error,datalist=ItemList,mostlist=most,leastlist=least)

minstock = 300
# =============================================== ITEMS =========================================================================?
@app.route('/Instantfoodproducts', methods=['GET', 'POST'])
def Instantfoodproducts():
    error = None;
    return render_template('itemextended.html', error=error,item=y,minstock=minstock)

@app.route('/UHTmilk', methods=['GET', 'POST'])
def UHTmilk():
    error = None;
    return render_template('ajaxjquery.html', error=error,datalist=ItemList,mostlist=most,leastlist=least)

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    print "WORKING = = = =  * * FUCKKKK"
    user = request.form['username']
    password = request.form['password']
    pis = " yu gi oh"
    printem(user,password)
    return json.dumps({'status':'OK','user':user,'pass':password,'pi':pis});

if __name__ == '__main__':
    app.run(debug=True)






