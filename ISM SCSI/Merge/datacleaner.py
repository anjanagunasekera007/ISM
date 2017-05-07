import csv
import time
import csv

customertrasnactionlist = []
cleantransactions = []

def readdata():
    print "Reading data"
    with open("../DATASETS/COMBIED_ITEMS.csv", 'rb') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            print row
            print type(row)
            customertrasnactionlist.append(row)



def cleanitems():
    # for transaction in customertrasnactionlist:
    #     for item in transaction:
    #         if(item):
    #             print "OK"
    #         else:
    #             transaction
    for transaction in customertrasnactionlist:
        transaction = filter(None,transaction)
        cleantransactions.append(transaction)




def returntransactions():
    readdata()
    cleanitems()
    for t in cleantransactions:
        print t
    print len(cleantransactions)
    return cleantransactions

# =================================== EXECUTION FUNCTION CALLS ===========
# readdata()
# cleanitems()
#
#
#
# print " = = = = = "
# time.sleep(5)
# print " = = = = = = = - = - = - = - = - - = -  - = - =- "
# for t in cleantransactions:
#     print t
# print len(cleantransactions)