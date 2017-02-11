__author__ = 'ZEUS'
import csv
import  time

print("Groery data set")

cr = csv.reader(open("finalrecords.csv","rb"))
counter =0

data =[]

for row in cr:
    print(row)
    data.append(row)

print("\n\n\n\n")
print("========================SET COMPLETED========================")

time.sleep(10)

for f in data:
    print(f)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


cl = []

def createCl(dataset):
    print("====Create a list of candidate item sets of size ONE ====")
    "Create a list of candidate item sets of size ONE"

    for transaction in dataset:
        for item in transaction:
            if not[item] in cl:
                cl.append([item])
    "frozen set becuse it will kind of a dictionary"
    return map(frozenset,cl)

time.sleep(10)

createCl(data)
cl.sort()
print("=============== ITEMS ========== " + str(len(cl)))
text_file = open("items.txt", "w")


for item in cl:
    print(item)
    text_file.write(str(item))
    text_file.write("\n")

text_file.close()

print("Write completed +++++++++++++++++++++")