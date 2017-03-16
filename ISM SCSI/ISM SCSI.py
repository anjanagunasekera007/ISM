from flask import Flask , render_template
from Sales_Calculator import returnSales
from Sales_Calculator import sortlist
# from Sales_Calculator import retunleastsold
import time
import sys


app = Flask(__name__)
app.config['DEBUG'] = True

#EXTERNAL FUNCTIONS


#External Functions
# newlist = []
# def sortlist():
#     newlist = sorted(ItemList, key=lambda x: x.soldTotal, reverse=True)
#     for j in newlist:
#         print type(newlist)
#         print j.name + " Q1 :" + str(j.soldQ1) + " Q2 :" + str(j.soldQ2) + " Q3 :" + str(j.soldQ3) + " Q4 :" + str(j.soldQ4) + " Q4 :" + str(j.soldTotal)
#     return newlist

# def returnmostsold():
#     sortlist()
#     print "SORTED"
#     time.sleep(3)
#     most = newlist[0:5]
#     print "MOST SOLD ITEMS ARE : ========================= "
#     for j in most:
#         print j.name + " TOTAL SALES :" + str(j.soldTotal)
#     return most
#
# def retunleastsold():
#     sortlist()
#     print "SORTED"
#     time.sleep(3)
#     least = newlist[164:]
#     print "LEASE SOLD ITEMS ARE : ======================== "
#     for j in least:
#         print j.name + " TOTAL SALES :" + str(j.soldTotal)
#     return least


#*************************************************************
ItemList = returnSales()
newlist = sortlist()
# print str(len(newlist))
# print " hoooooo "
# time.sleep(2)
most = newlist[0:5]
least = newlist[164:]
print "--------------------------------------------------------------- 8 8 8 ---------------------------------------"
# print str(len(ItemList))
# print str(len(most))
# print str(len(least))
# print " NEW LIST : " + str(len(newlist))
# sys.exit(89)



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

if __name__ == '__main__':
    app.run(debug=True)






