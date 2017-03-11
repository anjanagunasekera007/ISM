import csv
import time
import sys
from collections import defaultdict
import sys
db = []
#
# with open('item list.csv', 'rb') as f:
#     spamreader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in spamreader:
#         db.append(filter(None, row))
#     for h in db:
#         print h
#         # print ":_:"
# # sys.exit(444)
# print " = = = = = = = = = = = = = = = = = ="

#====================================================================================

# data = [["A","B","D","E"],
#         ["A","C","D"],
#         ["A","B","F","C"],
#         ["A","C","B"],
#         ["D","F","B"],
#         ["D","F","E"],
#         ["D","F"],
#         ["D","F","A"],
#         ["D","A","B"],
#         ["E","B","A","C"],
#         ["B","C","E"],
#         ["E","C","B","A"],
#         ["A","D","B"],
#         ["B","E","A","D"],
#         ["A","D","F"],]
#
# results = []
# minsup = 5
#
# for i in data:
#     print i
#
# print "---------------------------------"
# time.sleep(2)
# def run_100(patt, mdb):
#     results.append((patt, len(mdb)))
#     occurs = defaultdict(list)
#     for (i, startpos) in mdb:
#         seq = data[i]
#         # print "  - " + str(startpos) + "  to " + str(len(seq))
#         for j in xrange(startpos, len(seq)):
#             # print "ane yakooooooo wadakarpiyaaaaaaaaaaaaaaaaaaaaaa"
#             l = occurs[seq[j]]
#             if len(l) == 0 or l[-1][0] != i:
#                 l.append((i, j + 1))
#     for (c, newmdb) in occurs.iteritems():
#         if len(newmdb) >= minsup:
#             run_100(patt + [c], newmdb)
#
# run_100([], [(i, 0) for i in xrange(len(data))])
#
# for l in results:
#     print l
#
# sys.exit(23)

#====================================================================================
with open("../DATASETS/item list.csv",'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        print type(row)
        t = filter(None, row)
        db.append(t)

time.sleep(2)
print "prining the list"
time.sleep(1)
for i in db:
    print i
    print type(i)

def prune():
    print "lol pruning"




results = []
minsup = 300
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