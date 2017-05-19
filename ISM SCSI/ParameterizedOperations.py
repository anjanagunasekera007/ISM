import csv
import sys
import time

impactList = []

class Impact_overall:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, name, impactSize):
      self.name = name
      self.impactSize = impactSize

OLIST = []
def readImpact():
    p = []
    with open('D:/FYP/ISM SCSI/datasets/Instant food products.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for impact in readCSV:
            impactList.append(impact)
            print impact
            print type(impact)
            print impact[1]
            print type(impact[1])
            t = impact[1].split("=>")
            print str(len(t)) + " size" +  t[1]

            oimpact = Impact_overall(t[1],impact[3])
            p.append(oimpact)
            # print str(len(transaction))
            # print ";;;;;;;;;;;;;;;;;;;;;"
            # sys.exit(99999)
    print len(p)
    return p

readImpact()

# print len(OLIST)
#
#
# def returnImpacts():
#     readImpact()
#     print " = = = = = = =  " + str(len(OLIST))
#     return OLIST


# returnImpacts()
#
# j = returnImpacts()

# for u in OLIST:
#     print u.name
#     print u.impactSize

# print len(OLIST)