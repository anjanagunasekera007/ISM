import csv
import sys
import time

impactList = []

class Impact_overall:
   'Common base class for all employees'
   itemCount = 0

   def __init__(self, name, impactSize,chex):
      self.name = name
      self.impactSize = impactSize
      self.chex =  chex

OLIST = []
chexArray = ["#f15854","#decf3f","#b276b2","#b2912f","#f17Cb0","#60bd68","#faa43a","#5da5da","#4d4d4d","#433159","#f7c785"]
def readImpact(itemname):
    c =0
    p = []
    with open('D:/FYP/ISM SCSI/datasets/'+itemname+'.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for impact in readCSV:
            impactList.append(impact)
            print impact
            print type(impact)
            print impact[1]
            print type(impact[1])
            t = impact[1].split("=>")
            print str(len(t)) + " size" +  t[1]

            oimpact = Impact_overall(t[1],impact[3],chexArray[c])
            c = c+1
            p.append(oimpact)
            # print str(len(transaction))
            # print ";;;;;;;;;;;;;;;;;;;;;"
            # sys.exit(99999)
    print len(p)
    return p

# readImpact()

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