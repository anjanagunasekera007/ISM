import csv

myfile = open("ILIST.csv", 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

with open('groceries.csv', 'rb') as f:
     reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
     for row in reader:
        newrow =  ','.join(map(str, row))
        cleanedData = newrow.replace(",,", "")
        cleanedData = newrow.replace("|", "")
        cleanedData = newrow.replace(";", "")
        cleanedData = newrow.replace(":", "")
        print(cleanedData)
        itemList = cleanedData.split(",")
        wr.writerow(itemList)

print(type(newrow))
print(type(itemList))