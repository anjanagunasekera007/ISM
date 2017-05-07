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
  else:
    # Terminate
    print "Connection unsuccessful"

def checkPOS():
    #Since POS system is an emulated function which was implemented using JS
    return True

def checkAssociations():
    if os.path.isfile("D:\FYP\ISM SCSI\datasets\association_rules.csv"):
        return True
    else:
         return False

def checkClusters():
     if os.path.isfile("D:\FYP\ISM SCSI\Datasets\clusters.csv"):
        return True
     else:
         return False

def checkmetadata():
     if os.path.isfile("D:\FYP\ISM SCSI\datasets\alldata"):
         return True
     else:
         return False

def checkGroceries():
     if os.path.isfile("D:\FYP\ISM SCSI\datasets\groceries_cleaned"):
         return True
     else:
         return False

def initiateStartup():
    startupList = []

# ================================ EXECUTION FUCNTION CALLS  ==============

print checkDB()
print checkPOS()
print checkAssociations()
print checkClusters()
print checkGroceries()
print checkGroceries()
