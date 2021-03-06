# lst = ["He", "is", "so", "", "cool"]
# filter(None, lst)
#
# print filter(None, lst)


#! /usr/bin/env python
import csv
import time

import sys
from collections import defaultdict

# db = [["A","B","C"],["A"],["B"],["C","D"],["A","B","D"],["A","B","E"],["A","B","C"],["A","B","C","D","E"]]
db = []
customertransactionlist = []

with open('item list.csv', 'rb') as f:
    spamreader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        db.append((filter(None, row)))


def readitemlists():
    counter = 0
    with open('item list.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for transaction in readCSV:
            print filter(None, transaction)
            customertransactionlist.append(filter(None, transaction))
            print type(transaction)
            counter = counter + 1
            # print str(len(readCSV))
            print str(counter)
print ("=============================")
print(len(db))

readitemlists()
for items in customertransactionlist:
    print items
    print "    " + str(type(items))


results = []
minsup = 8
print ("Initiating frequest item list generation")
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

run_100([], [(i, 0) for i in xrange(len(db))])

print (type(results))

for t in results:
    print t
sys.exit(78)