__author__ = 'ZEUS'

import grocery_apriori as apriori

dataset = apriori.load_dataset()

print("***The data set has been loaded and is in:dataset:")
print(dataset)
print(" ")
print(" ")
print(" ")

print("*** Creating the candidate item set c1 contains a list with all items in frozen set")
c1 = apriori.createCl(dataset)
print(c1)
print(" ")
print(" ")
print(" ")