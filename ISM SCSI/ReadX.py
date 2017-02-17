import csv

ClusterList = []
ItemList = []

C1 = []
C2 = []
C3 = []
C4 = []
C5  = []
C6  = []
C7 = []


f = open("./ex/clusters123.txt")
for month in f.readlines():
   t = month.split(",")
   print type(t)
   print len(t)

   for num in t:
       num = int(num)
       ClusterList.append(num)


print (len(ClusterList))

for j in ClusterList:
    if(j ==1):
        C1.append(j)
    if(j ==2):
        C2.append(j)
    if(j ==3):
        C3.append(j)
    if(j ==4):
        C4.append(j)
    if(j ==5):
        C5.append(j)
    if(j ==6):
        C6.append(j)
    if(j ==7):
        C7.append(j)


print "======================"
print len(C1)
print len(C2)
print len(C3)
print len(C4)
print len(C5)
print len(C6)
print len(C7)



with open("./ex/ITEM_MERGE_20170217_C.csv",'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
        ItemList.append(row)
        for r in row:
             print r
        print "== END =="

print " 0 0 0 0 "
print len(ItemList)
print len(ClusterList)