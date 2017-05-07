import csv
import time
import  sys

minedcategorylist = []

def read():
    with open("../DATASETS/frequentitems.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            print row
            print type(row)
            print len(row)
            print row[0]
            mlist = row[0].split(",")
            print " MLIST CREATED"
            print mlist[0]
            categorylist = []
            for t in mlist:
                t =t.replace("[","")
                t = t.replace("'","")
                t = t.replace("]","")
                categorylist.append(t)

            tr = mlist[0].replace("[","")
            tr = tr.replace("'","")
            print tr
            print len(tr)
            print "\n"
            print "\n"
            print "\n"

            # print "0 : "
            # print row[0]
            # print type(row[0])
            # print "LENGTH OF row[0] => " + str(len(row[0]))
            # print "----------------------------"
            # print "1 : "
            # print row[1]
            # print "----------------------------"


# ================================== EXECUTIONS FUNCTION CALLS
read()