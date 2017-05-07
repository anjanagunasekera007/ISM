import csv
import time
import sys

segmentlist = []
seg1 = []
seg2 = []
seg3 = []
seg4 = []
seg5 = []
seg6 = []
seg7 = []
seg8 = []
seg9 = []


def readCustomers():
    print "Reading customers"
    with open("../DATASETS/clusters.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            print row
            print type(row)
            print len(row)
            for item in row:
                print item
                print type(item)
                segmentlist.append(item)



def printsegmentlist():
    for t in segmentlist:
        print t
        print type(t)

def returnsegmentlist():
    readCustomers()
    time.sleep(2)
    printsegmentlist()
    print " = = = = = = = = "
    print len(segmentlist)
    return segmentlist

# ============================= EXECUTIONS AND FUNCTION CALLS =================
# readCustomers()
# time.sleep(2)
# printsegmentlist()
# print " = = = = = = = = "
# print len(segmentlist)