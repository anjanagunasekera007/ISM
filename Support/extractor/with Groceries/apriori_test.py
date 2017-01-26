__author__ = 'ZEUS'

import apriori_1 as apriori

dataset = apriori.load_dataset()

print("***The data set has been loaded and is in:dataset:")
print(dataset)
print(" ")
print(" ")
print(" ")

print("*** Creating the candidate item set c1 contains a list with all items in frozen set")
c1 = apriori.createCl(dataset)
print(c1)

f = open('items.txt', 'w')

for item in c1:
    f.write(str(item)  + "\n")

# f.write(c1)  # python will convert \n to os.linesep
f.close()  # you can omit in most cases as the destructor will call it

print(" ")
print(" ")
print(" ")

print("***D is a data set in the form of a list of sets")
D = map(set,dataset)
print(D)
print(" ")
print(" ")
print(" ")

print("***In L1 we have removed every item that does not support our  minimum requirement ex 0.5")
print("The result is represent by the list L1 created")
L1,support_data = apriori.scanD(D,c1,0.5)
print(L1)
print(" ")
print(" ")
print(" ")

print "  +++++++++++++++++++++++++++++++++++++++++++++++++END OF SECTION 1 +++++++++++++++++++++++++++++++++++++++++++  "
print(" in the above section finally we have removed items that dioes not support the minmium support of 0.5")
print("To calculate support manually count:1: for each set which contains the item and write it as a fraction of the total item sets")
print("")
print("")
print("")


print("Now we shall use aprioriGen to generate the next list of candidate item sets")
print("when it generates item sets scanD will will throw out elements that ")
print("We are passing :2: as a constatnt to generate TWO ITEM sets that means sets with two items each")
#apriori.aprioriGen(L1,2)
print(apriori.aprioriGen(L1,2))
print("")
print("")
print("")


print("If we run it with our apriori function we will check that L contains some lists of frequent itemsets that met a minimum support of 0.5. ")
L = apriori.apriori(dataset)
print(L)


print("Generating rules ")
print("==============================")

L,support_data = apriori.apriori(dataset)

print(apriori.generateRules(L,support_data,min_confidence=0.5))






