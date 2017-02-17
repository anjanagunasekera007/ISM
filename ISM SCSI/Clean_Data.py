# import csv
#
# myfile = open("ILIST.csv", 'wb')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#
#
#
#
# with open('groceries.csv', 'rb') as f:
#      reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
#      for row in reader:
#          # print row
#         newrow =  ','.join(map(str, row))
#         # print newrow
#         purified =  newrow.replace(",,", "")
#         print(purified)
#         itemList = purified.split(",")
#         wr.writerow(itemList)
#
#
#
#
# print(type(newrow))
# print(type(itemList))

import csv
counter =0
with open('./ex/added.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        counter = counter + 1
        print row
        # t = ', '.join(row)
        # t = t.replace(",,","")
        # for it in row:
        #     print it