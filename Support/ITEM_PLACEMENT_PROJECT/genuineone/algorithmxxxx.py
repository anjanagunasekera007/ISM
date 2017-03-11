#! /usr/bin/env python
import csv
import time
import sys

import sys
from collections import defaultdict

# db = [["A","B","C"],["A"],["B"],["C","D"],["A","B","D"],["A","B","E"],["A","B","C"],["A","B","C","D","E"]]
db = []


with open('item list.csv', 'rb') as f:
    spamreader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        db.append(filter(None, row))
    for h in db:
        print h
        # print ":_:"
sys.exit(444)
print " = = = = = = = = = = = = = = = = = ="
# sys.exit(70)



print ("=============================")
print(len(db))

for items in db:
    print items
    print "    " + str(type(items))

time.sleep(2)
minsup = int(3)

print ("PAUSE")
print ("GENERATING FREQUENT ITEM SETS WITH A MINIMUM OF " + str(minsup) +  " OCCOURENCES")
time.sleep(2)
print ("BEGIN")

# minsup = int(8)

results = []

print ("Initiating frequest item list generation")
def run_100(patt, mdb):
    results.append((patt, len(mdb)))
    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        # print "  - " + str(startpos) + "  to " + str(len(seq))
        for j in xrange(startpos, len(seq)):
            # print "ane yakooooooo"
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))
    for (c, newmdb) in occurs.iteritems():
        if len(newmdb) >= minsup:
            run_100(patt + [c], newmdb)

run_100([], [(i, 0) for i in xrange(len(db))])

print (type(results))

for l in results:
    print l
