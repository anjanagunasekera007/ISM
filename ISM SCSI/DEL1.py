from DBHandler import updateReOrderStatus
import sys
import time
from DBHandler import inversePOS
from DBHandler import  inverseSTOCKDEPETER
#
#
# print " INITIATING"
# updateReOrderStatus("Instant food products","On order")
# print " DONE"

print " INVERSING NOW"
inversePOS()
inverseSTOCKDEPETER()
print " END OF INVERSE CHECK DB NOW"
