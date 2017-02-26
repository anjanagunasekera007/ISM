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


with open('item list.csv', 'rb') as f:
    spamreader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in spamreader:
        db.append(row)


print ("=============================")
print(len(db))

for items in db:
    print items
    print "    " + str(type(items))