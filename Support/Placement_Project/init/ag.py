#! /usr/bin/env python
import csv
import time

import sys
from collections import defaultdict


db = []


with open('item list.csv', 'rb') as f:
    spamreader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        db.append(row)


print ("=============================")
print(len(db))

for items in db:
    print items

minsup = int(8)

print ("PAUSE")
print ("GENERATING FREQUENT ITEM SETS WITH A MINIMUM OF " + str(minsup) +  " OCCOURENCES")
time.sleep(2)
print ("BEGIN")

# minsup = int(8)

results = []

print ("ahaaaaaaa")
def mine_rec(patt, mdb):
    results.append((patt, len(mdb)))
    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = db[i]
        print " in for  - - "
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            if len(l) == 0 or l[-1][0] != i:
                l.append((i, j + 1))
    for (c, newmdb) in occurs.iteritems():
        if len(newmdb) >= minsup:
            print "found more than minsupport"
            mine_rec(patt + [c], newmdb)

            # call
mine_rec([], [(i, 0) for i in xrange(len(db))])

print (type(results))

# for l in results:
#     print l
