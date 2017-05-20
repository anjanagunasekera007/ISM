import sys
import time
import csv

from datacleaner import returntransactions
from clusterreader import returnsegmentlist
from collections import defaultdict
# transactions = []
# segments = []



# seglist = returnsegmentlist()
#
# for i in seglist:
#     print i
#
# sys.exit(3456)


class Fpattern:

   def __init__(self, items,support):
      self.items = items
      self.support = support

class CSegment:
    def __init__(self, segmentid, size):
        self.segmentid = segmentid
        self.size = size

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



def explode(transactions,segments):
    print len(segments)
    print len(transactions)
    time.sleep(3)
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
results = []
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


def getfrequentItems(transactionsList):
    # db = []
    for t in transactionsList:
        print type(t)
        db.append(t)
    print len(transactionsseg1)

    run_100([], [(i, 0) for i in xrange(len(db))])

#========================================

# ============================ EXECUTIONS FUNCTION CALLS =============



def returnSegments():
    transactions = returntransactions()
    segments = returnsegmentlist()
    explode(transactions,segments)
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
    segmentlist = []
    n1 = CSegment(1,len(seg1))
    n2 = CSegment(2, len(seg2))
    n3 = CSegment(3, len(seg3))
    n4 = CSegment(4, len(seg4))
    n5 = CSegment(5, len(seg5))
    n6 = CSegment(6, len(seg6))
    n7 = CSegment(7, len(seg7))
    n8 = CSegment(8, len(seg8))
    n9 = CSegment(9, len(seg9))
    segmentlist.append(n1)
    segmentlist.append(n2)
    segmentlist.append(n3)
    segmentlist.append(n4)
    segmentlist.append(n5)
    segmentlist.append(n6)
    segmentlist.append(n7)
    segmentlist.append(n8)
    segmentlist.append(n9)

    for u in segmentlist:
        print u.size
    # sys.exit(747)

    return segmentlist

def returnFrequenetPaterns():
    getfrequentItems(transactionsseg1)
    getfrequentItems(transactionsseg2)
    getfrequentItems(transactionsseg3)
    getfrequentItems(transactionsseg4)
    getfrequentItems(transactionsseg5)
    getfrequentItems(transactionsseg6)
    getfrequentItems(transactionsseg7)
    getfrequentItems(transactionsseg8)
    getfrequentItems(transactionsseg9)

# returnSegments()
# sys.exit(99)
# time.sleep(3)

getfrequentItems(transactionsseg1)

patternlist = []
print " DONE "
# time.sleep(2)
for y in results:
    print y
    p = Fpattern(y[0],y[1])
    patternlist.append(p)
    # print type(y[0])
    # print y[0]
    # print type(y[1])
    # print y[1]
    # print len(y)
    print "\n"
print " ======================== "
time.sleep(2)
for i in patternlist:
    print i.items
    print str(type(i.items)) + "   " + str(i.support)

# sys.exit(77)
patternlist.sort(key=lambda x: x.support, reverse=True)
print " ; ; ; ; ; ; ; ; ; ; ; ; ; ; ; ; ; "
time.sleep(2)

for u in patternlist:
    print u.support

print " + + + + "
metList = patternlist[0:5]
print len(metList)

print "..................................................................."
print " FREQUENT ITEMS OF C1"
fitemlist = []
for y in metList:
    fitemlist.append(y.items)
    print y.items
    print y.support
print "...................................................................."


def returnFREQUENTITEMS():
    seg1Items = []
    p1 = Fpattern("ice cream",35)
    p2 = Fpattern("waffles", 35)
    p3 = Fpattern("chewing gum'", 35)
    seg1Items.append(p1)
    seg1Items.append(p2)
    seg1Items.append(p3)

    seg2Items = []
    p1 = Fpattern("waffles",35)
    p2 = Fpattern("beef", 35)
    p3 = Fpattern("berries'", 30)
    seg2Items.append(p1)
    seg2Items.append(p2)
    seg2Items.append(p3)

    seg3Items = []
    p1 = Fpattern("cereals",30)
    p2 = Fpattern("chicken", 30)
    p3 = Fpattern("bottled water'", 30)
    seg3Items.append(p1)
    seg3Items.append(p2)
    seg3Items.append(p3)

    seg4Items = []
    p1 = Fpattern("cleaner",22)
    p2 = Fpattern("candles", 19)
    p3 = Fpattern("curd'", 18)
    seg4Items.append(p1)
    seg4Items.append(p2)
    seg4Items.append(p3)

    seg5Items = []
    p1 = Fpattern("cocoa drinks",64)
    p2 = Fpattern("coffee", 62)
    p3 = Fpattern("cookware'", 59)
    seg5Items.append(p1)
    seg5Items.append(p2)
    seg5Items.append(p3)

    seg6Items = []
    p1 = Fpattern("cocoa drinks",356)
    p2 = Fpattern("frankfurter", 340)
    p3 = Fpattern("domestic eggs'", 336)
    seg6Items.append(p1)
    seg6Items.append(p2)
    seg6Items.append(p3)

    seg7Items = []
    p1 = Fpattern("cream cheese ",58)
    p2 = Fpattern("cream", 58)
    p3 = Fpattern("dishes", 58)
    seg7Items.append(p1)
    seg7Items.append(p2)
    seg7Items.append(p3)

    seg8Items = []
    p1 = Fpattern("flour ",35)
    p2 = Fpattern("fish", 35)
    p3 = Fpattern("pork", 35)
    seg8Items.append(p1)
    seg8Items.append(p2)
    seg8Items.append(p3)

    seg9Items = []
    p1 = Fpattern("ready soups ",35)
    p2 = Fpattern("pastry", 35)
    p3 = Fpattern("oil", 35)
    seg9Items.append(p1)
    seg9Items.append(p2)
    seg9Items.append(p3)

    segitemlist = []
    segitemlist.append(seg1Items)
    segitemlist.append(seg2Items)
    segitemlist.append(seg3Items)
    segitemlist.append(seg4Items)
    segitemlist.append(seg5Items)
    segitemlist.append(seg6Items)
    segitemlist.append(seg7Items)
    segitemlist.append(seg8Items)
    segitemlist.append(seg9Items)

    return segitemlist
