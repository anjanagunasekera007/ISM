import csv
import time
import sys

print "Begin operation"


db = []
categorylist = [["Miscellaneous", "C1"],
                ["Dairy Products", "C2"],
                ["Cleaning Items", "C3"],
                ["Grocery Items", "C4"],
                ["Fish and Meat", "C5"],
                ["Fruits and Vegetables", "C6"],
                ["Beverages", "C7"],
                ["Liquor", "C8"],
                ["Pet Food", "C9"],
                ["Kitchenware", "C10"],
                ["Gardening Product", "C11"],
                ["Frozen Food Items", "C12"],
                ["Cosmetic Item", "C13"],
                ["Processed Meat Products", "C14"]
                ]
itemlistwithcategories = []

def readitemlist():
    with open("../DATASETS/Categories of items.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            # print row
            # print type(row)
            t = filter(None, row)
            db.append(t)

    time.sleep(2)
    counter = 0
    print "prining the list"
    time.sleep(1)
    for i in db:
        print i
        print type(i)
        print counter
        print "\n"
        counter = counter + 1

def createcategorylist():
    myfile = open("../DATASETS/categories.csv", 'wb')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for line in categorylist:
        wr.writerow(line)

def replacecategoryinlist():
    for row in db:
        t = filter(None, row)
        itemlistwithcategories.append(t)

    for h in itemlistwithcategories:
        print h
        print str(len(h))
        print type(h)


def replacer():
    for item in itemlistwithcategories:
        if item[2]=="Miscellaneous ":
            item.append("C1")
        if item[2]=="Dairy Products ":
            item.append("C2")
        if item[2]=="Cleaning Items ":
            item.append("C3")
        if item[2]=="Grocery Items":
            item.append("C4")
        if item[2]=="Baby Products":
            item.append("C5")
        if item[2]=="Fish and Meat ":
            item.append("C6")
        if item[2]=="Fruits and Vegetables ":
            item.append("C7")
        if item[2]=="Beverages ":
            item.append("C8")
        if item[2]=="Liquor":
            item.append("C9")
        if item[2]=="Pet Food":
            item.append("C10")
        if item[2]=="Kitchenware":
            item.append("C11")
        if item[2]=="Gardening Product":
            item.append("C12")
        if item[2]=="Frozen Food Items":
            item.append("C13")
        if item[2]=="Cosmetic Item":
            item.append("C14")
        if item[2]=="Processed Meat Products":
            item.append("C15")







print "creating list"
readitemlist()

createcategorylist()

for t in categorylist:
    print t

time.sleep(2)
print "\n"
print "\n"
replacecategoryinlist()

replacer()

for j in itemlistwithcategories:
    print j
print "completed"