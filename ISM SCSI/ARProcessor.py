import csv
import sys
import time
import os.path
from Association_Class import Association
megalist = []
associations = []

#=======================
def read():
    with open("D:/FYP/ISM SCSI/datasets/association_rules.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            # print "       -  " + str(row[0])
            # print type(row[0])
            # print "       -  " + str(row[1])
            # print type(row[1])
            # print "       -  " + str(row[2])
            # print type(row[2])
            # print "       -  " + str(row[3])
            # print type(row[3])
            # print "       -  " + str(row[4])
            # print type(row[4])
            # print type(row)
            # print row
            ar = Association(row[1],row[2],row[3],row[4])
            associations.append(ar)
#======================
def printAssociations():
    for i in associations:
        print type(i)
        print i.rule

def returnAssociations():
    return associations
# def read():
#     with open("../DATASETS/association_rules.csv", 'rb') as f:
#         reader = csv.reader(f)
#         counter = 0
#         for row in reader:
#             print type(row)
#             print row
#             print len(row)
#             print " * * * * * * "
#             print type(row[1])
#             mlist = row[1].split("=>")
#
#             print type(mlist[0])
#             print type(mlist[1])
#             print " : : : : : :  : : : : : : : : : : : : "
#             mlist[0] = mlist[0].replace("{","")
#             mlist[0] = mlist[0].replace("}", "")
#             mlist[0] = mlist[0].replace("[", "")
#             mlist[0] = mlist[0].replace("]", "")
#             mlist[1] = mlist[1].replace("{","")
#             mlist[1] = mlist[1].replace("}", "")
#             mlist[1] = mlist[1].replace("{", "")
#             mlist[1] = mlist[1].replace("[", "")
#             mlist[1] = mlist[1].replace("]", "")
#             print mlist
#             print row[3]
#             print " : : : : : :  : : : : : : : : : : : : "
#             clist= []
#             clist.append(mlist)
#             clist.append(row[3])
#             megalist.append(clist)
#
#             print "\n"
#             print "\n"
#             print "\n"
#
#
# def printmegalist():
#     print " +*-*+*-*+*-*+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+*-+--*"
#     time.sleep(4)
#     print "\n"
#     print "\n"
#     for t in megalist:
#         print t
#         print len(t)
#         print type(t[0])
#         print type(t[1])
#
# def  writelist():
#     with open("../DATASETS/ARS.csv", 'wb') as resultFile:
#         wr = csv.writer(resultFile, dialect='excel')
#         for t in megalist:
#             wr.writerow(t)
# =================== EXECUTION FUNCTION CALLS
read()
printAssociations()
# printmegalist()
# writelist()


# print (os.path.exists("../DATASETS/association_rules.csv"))
# print (os.path.exists("../DATASETS/LOL.csv"))
# print (os.path.exists("../DATASETS/all_items.txt"))
# print (os.path.exists("../DATASETS/groceries_cleaned.csv"))