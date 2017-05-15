status = []
import os.path
import MySQLdb

def checkDB():
  # Connect to the MySQL database
  db = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'ism')

  # Check if connection was successful
  if (db):
    # Carry out normal procedure
    print "Connection successful"
    return True
  else:
    # Terminate
    print "Connection unsuccessful"
    return False

def checkPOS():
    #Since POS system is an emulated function which was implemented using JS
    return True

def checkAssociations():
    if os.path.isfile("D:\FYP\ISM SCSI\datasets/association_rules.csv"):
        return True
    else:
         return False

def checkClusters():
     if os.path.isfile("D:\FYP\ISM SCSI\Datasets/clusters.csv"):
        return True
     else:
         return False

def checkmetadata():
     if os.path.isfile("D:\FYP\ISM SCSI\datasets/alldata.csv"):
         return True
     else:
         return False

def checkGroceries():
     if os.path.isfile("D:\FYP\ISM SCSI\datasets\groceries_cleaned.csv"):
         return True
     else:
         return False

def initiateStartup():
    startupList = []
    db = checkDB()
    print "CHECK DB  " + str(db)

    pos = checkPOS()
    print "CHECK POS  " + str(pos)

    associations = checkAssociations()
    print "CHECK ASSOCIATIONS  " + str(associations)

    clusters = checkClusters()
    print "CHECK CLUSTERS  " + str(clusters)

    metadata = checkmetadata()
    print "CHECK CHECK GROCERIES  " + str(metadata)

    groceries = checkGroceries()
    print "CHECK CHECK GROCERIES  " + str(groceries)
    startupList.append(db)
    startupList.append(pos)
    startupList.append(associations)
    startupList.append(clusters)
    startupList.append(metadata)
    startupList.append(groceries)

    return startupList

# ================================ EXECUTION FUCNTION CALLS  ==============

print "CHECK DB  " + str(checkDB())
print "CHECK POS  " + str(checkPOS())
print "CHECK ASSOCIATIONS  " + str(checkAssociations())
print "CHECK CLUSTERS  " + str(checkClusters())
print "CHECK CHECK GROCERIES  " + str(checkmetadata())
print "CHECK CHECK GROCERIES  " + str(checkGroceries())
# print checkGroceries()
