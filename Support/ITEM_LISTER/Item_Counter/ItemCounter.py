from Item import Item

transactions = [["A","B","D"],["A","B"],["A","B","D","E"],["A","C"]]

itemdb = []

def itemlistmaker():
    item1 = Item("A")
    item2 = Item("B")
    item3 = Item("C")
    item4 = Item("D")
    item5 = Item("E")
    itemdb.append(item1)
    itemdb.append(item2)
    itemdb.append(item3)
    itemdb.append(item4)
    itemdb.append(item5)

itemlistmaker()

for items in itemdb:
    print (items.name + " " + str(items.sold))
print ("============================")
for items in transactions:
    print items

print (" = = = = = = = = = = = = = = = ")
print (" = = = = = = = = = = = = = = = ")

print (" = = = = = = = = = = = = = = = ")
#
for items in transactions:
    for unit in items:
        for dbitem in itemdb:
            if dbitem.name == unit:
                print ( dbitem.name + " MATCH FOUND " + unit)
                dbitem.sold = dbitem.sold + 1
                print ("UPPED")


print " 9999999999999999999999999  "

for tracks in itemdb:
    print tracks.name + "  " + str(tracks.sold)