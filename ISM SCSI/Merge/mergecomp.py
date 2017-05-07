import sys
import time
import csv

from datacleaner import returntransactions
from clusterreader import returnsegmentlist
from collections import defaultdict
transactions = []
segments = []

seg1 = []
seg2 = []
seg3 = []
seg4 = []
seg5 = []
seg6 = []
seg7 = []
seg8 = []
seg9 = []
transactionsseg1 = []
transactionsseg2 = []
transactionsseg3 = []
transactionsseg4 = []
transactionsseg5 = []
transactionsseg6 = []
transactionsseg7 = []
transactionsseg8 = []
transactionsseg9 = []

results = []

def explode():
    index = 0
    for customer in segments:
        print customer
        if(customer=="1"):
            seg1.append(customer)
            transactionsseg1.append(transactions[index])
            index = index +1
            print " MATCHED "
        elif(customer=="2"):
            seg2.append(customer)
            transactionsseg2.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="3"):
            seg3.append(customer)
            transactionsseg3.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="4"):
            seg4.append(customer)
            transactionsseg4.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="5"):
            seg5.append(customer)
            transactionsseg5.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="6"):
            seg6.append(customer)
            transactionsseg6.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="7"):
            seg7.append(customer)
            transactionsseg7.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="8"):
            seg8.append(customer)
            transactionsseg8.append(transactions[index])
            index = index + 1
            print " MATCHED "
        elif(customer=="9"):
            seg9.append(customer)
            transactionsseg9.append(transactions[index])
            index = index + 1
            print " MATCHED "

#=======================================
db = []
print ("Initiating frequest item list generation")
minsup = 3
def run_100(patt, mdb):
    results.append((patt, len(mdb)))
    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        print "  - " + str(startpos) + "  to " + str(len(seq))
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))
    for (c, newmdb) in occurs.iteritems():
        if len(newmdb) >= minsup:
            run_100(patt + [c], newmdb)


def getfrequentItems():

    for t in transactionsseg1:
        print type(t)
        db.append(t)
    print len(transactionsseg1)

    run_100([], [(i, 0) for i in xrange(len(db))])

#========================================

# ============================ EXECUTIONS FUNCTION CALLS =============
transactions = returntransactions()
segments = returnsegmentlist()
explode()
print " - - - - - - - - - -"
print len(transactions)
print len(segments)

print "1  => " + str(len(seg1)) + " = " + str(len(transactionsseg1))
print "2  => " + str(len(seg2)) + " = " + str(len(transactionsseg2))
print "3  => " + str(len(seg3)) + " = " + str(len(transactionsseg3))
print "4  => " + str(len(seg4)) + " = " + str(len(transactionsseg4))
print "5  => " + str(len(seg5)) + " = " + str(len(transactionsseg5))
print "6  => " + str(len(seg6)) + " = " + str(len(transactionsseg6))
print "7  => " + str(len(seg7)) + " = " + str(len(transactionsseg7))
print "8  => " + str(len(seg8)) + " = " + str(len(transactionsseg8))
print "9  => " + str(len(seg9)) + " = " + str(len(transactionsseg9))
# sys.exit(89)
print " - - - - - - - - "
time.sleep(3)
getfrequentItems()

print " DONE "
time.sleep(2)
for y in results:
    print y
    # print type(y[0])
    print y[0]
    # print type(y[1])
    print y[1]
    # print len(y)
    print "\n"
