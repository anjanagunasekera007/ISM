import csv
import sys
import time
# from Item_Category_Class import ItemC
from collections import defaultdict
import timeit

l1p = []
l2p = []
l3p = []
l4p = []

print "BEGIN"

itemobjectlist = []
transactionlist = []
db = []
results = []

# def read():
#         with open("../DATASETS/category list.csv", 'rb') as f:
#             reader = csv.reader(f)
#             counter = 0
#             for row in reader:
#                 # print row
#                 # print type(row)
#                 t = filter(None, row)
#                 # db.append(t)
#                 item = ItemC(t[0],t[1],t[2])
#                 print t
#                 print type(t)
#                 print str(len(t))
#                 print "COUNTER : " + str(counter)
#                 itemobjectlist.append(item)
#                 counter = counter +1



def readtransactionlist():
    print "reading transactions"
    with open("../DATASETS/item list.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            # f.append(row)
            print row
            transactionlist.append(row)
            # print row
            # print type(row)
            # t = filter(None, row)
            # print t

def replacce():
    print "replacing"
    for transaction in transactionlist:
        n = []
        print transaction
        for item in transaction:
            print item
            for iditem in itemobjectlist:
                if iditem.name == item:
                    print " ====================== match found"
                    n.append(iditem.categoryid)
        db.append(n)


    myfile = open("../DATASETS/replaceditemlist.csv", 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for line in db:
        wr.writerow(line)


def printcategorylist():
    print "reading transactions"
    with open("../DATASETS/replaceditemlist.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            # f.append(row)
            print row
            print type(row)
            print str(len(row))
            print "\n"
            counter = counter ++1


print ("Initiating frequest item list generation")
minsup = 120
def run_100(patt, mdb):
    results.append((patt, len(mdb)))
    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))
    for (c, newmdb) in occurs.iteritems():
        if len(newmdb) >= minsup:
            run_100(patt + [c], newmdb)

# run_100([], [(i, 0) for i in xrange(len(db))])

def l1patterns():
    run_100([], [(i, 0) for i in xrange(len(db))])

def l2patterns():
    run_100([], [(i, 0) for i in xrange(len(db))])

def l3patterns():
    run_100([], [(i, 0) for i in xrange(len(db))])

def l4patterns():
    run_100([], [(i, 0) for i in xrange(len(db))])
print " ==================================== "
readtransactionlist()

l1 = transactionlist[0:2450]
l2 = transactionlist[2451:4900]
l3 = transactionlist[4900:7350]
l4 = transactionlist[7350:9800]

l1patterns()
for t in results:
    print t
print len(results)


print len(l1p)
print len(l2p)
print len(l3p)
print len(l4p)


print "\n"
print len(transactionlist)


print " ==================================== "
sys.exit(78)
# read()
# sys.exit(1)
readtransactionlist()
# sys.exit(2)
# replacce()
# time.sleep(2)
# start_time = timeit.default_timer()
# run_100([], [(i, 0) for i in xrange(len(db))])
# elapsed = timeit.default_timer() - start_time
# print "--------------------"
# print elapsed
# print "--------------------"
# sys.exit(56)
# time.sleep(2)
# for u in results:
    # print u
    # print "\n"
# printcategorylist()
# print "--------------------"
# print " RESULTS : "
# for item in results:
#         print item
#         print type(item)
#         print str(len(item))
#         print "\n"

# print " COMPLETED"
# print " Attempting to write : . . . "
# myfile = open("../DATASETS/20170319.csv", 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#
# for item in results:
#     wr.writerow(item)

# print "WRITING COMPLETED"
# print "EXITING NOW"