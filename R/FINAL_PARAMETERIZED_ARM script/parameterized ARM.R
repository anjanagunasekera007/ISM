#Loading data
library(arules)
library(arulesViz)
library(datasets)

#load data set groceries 
data(Groceries)

#***********************************************UHT-milk*************************************************
print("Commencing Specialized association rule mining for -  UHT-milk - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="UHT-milk"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\UHT-milk.csv", sep = ",")
#************************************************************************************************

#*********************************************abrasive cleaner***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="abrasive cleaner"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\abrasive cleaner.csv", sep = ",")
#************************************************************************************************

#*********************************************Instant food products***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="Instant food products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\Instant food products.csv", sep = ",")
#************************************************************************************************

#*********************************************artif. sweetener***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="artif. sweetener"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\artif sweetener.csv", sep = ",")
#************************************************************************************************

#*********************************************baby cosmetics***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="baby cosmetics"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\baby cosmetics.csv", sep = ",")
#************************************************************************************************

#*********************************************baby food***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="baby food"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\baby food.csv", sep = ",")
#************************************************************************************************

#*********************************************bags***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="bags"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\bags.csv", sep = ",")
#************************************************************************************************


#*********************************************baking powder***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="baking powder"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\baking powder.csv", sep = ",")
#************************************************************************************************

#*********************************************bathroom cleaner***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="bathroom cleaner"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\bathroom cleaner.csv", sep = ",")
#************************************************************************************************

#*********************************************beef***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="beef"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\beef.csv", sep = ",")
#************************************************************************************************

#*********************************************berries***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="berries"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\berries.csv", sep = ",")
#************************************************************************************************

#*********************************************beverages***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="beverages"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\beverages.csv", sep = ",")
#************************************************************************************************

#*********************************************bottled beer***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="bottled beer"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\bottled beer.csv", sep = ",")
#************************************************************************************************

#*********************************************bottled water***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="bottled water"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\bottled water.csv", sep = ",")
#************************************************************************************************


#*********************************************brandy***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="brandy"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\brandy.csv", sep = ",")
#************************************************************************************************

#*********************************************brown bread***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="brown bread"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\brown bread.csv", sep = ",")
#************************************************************************************************

#*********************************************butter***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="butter"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\butter.csv", sep = ",")
#************************************************************************************************

#*********************************************butter milk***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="butter milk"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\butter milk.csv", sep = ",")
#************************************************************************************************

#*********************************************cake bar***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cake bar"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cake bar.csv", sep = ",")
#************************************************************************************************

#*********************************************candles***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="candles"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\candles.csv", sep = ",")
#************************************************************************************************


#*********************************************candy***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="candy"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\candy.csv", sep = ",")
#************************************************************************************************

#*********************************************canned beer***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="canned beer"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\canned beer.csv", sep = ",")
#************************************************************************************************

#*********************************************canned fish***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="canned fish"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\canned fish.csv", sep = ",")
#************************************************************************************************

#*********************************************canned fruit***************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="canned fruit"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\canned fruit.csv", sep = ",")
#************************************************************************************************

#*********************************************canned vegetables**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="canned vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\canned vegetables.csv", sep = ",")
#************************************************************************************************

#*********************************************cat food**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cat food"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cat food.csv", sep = ",")
#************************************************************************************************

#*********************************************cereals**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cereals"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cereals.csv", sep = ",")
#************************************************************************************************

#*********************************************chewing gum**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="chewing gum"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\chewing gum.csv", sep = ",")
#************************************************************************************************

#*********************************************cchicken**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="chicken"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\chicken.csv", sep = ",")
#************************************************************************************************

#*********************************************chocolate**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="chocolate"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\chocolate.csv", sep = ",")
#************************************************************************************************


#*********************************************chocolate marshmallow**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="chocolate marshmallow"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\chocolate marshmallow.csv", sep = ",")
#************************************************************************************************

#*********************************************citrus fruit**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="citrus fruit"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\citrus fruit.csv", sep = ",")
#************************************************************************************************

#*********************************************cleaner**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cleaner"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cleaner.csv", sep = ",")
#************************************************************************************************

#*********************************************cling film/bags**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cling film/bags"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cling.csv", sep = ",")
#************************************************************************************************

#*********************************************cocoa drinks**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cocoa drinks"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cocoa drinks.csv", sep = ",")
#************************************************************************************************

#*********************************************coffee**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="coffee"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\coffee.csv", sep = ",")
#************************************************************************************************

#*********************************************condensed milk**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="condensed milk"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\condensed milk.csv", sep = ",")
#************************************************************************************************

#*********************************************cooking chocolate**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cooking chocolate"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cooking chocolate.csv", sep = ",")
#************************************************************************************************

#*********************************************cookware**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cookware"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cookware.csv", sep = ",")
#************************************************************************************************

#*********************************************cream**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="cream"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cream.csv", sep = ",")
#************************************************************************************************

#*********************************************cream cheese **************************************************
#print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
#rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
#             appearance = list(default="rhs",lhs="cream cheese"),
#            control = list(verbose=F))

#eresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
#write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\cream cheese.csv", sep = ",")
#************************************************************************************************

#*********************************************curd**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="curd"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\curd.csv", sep = ",")
#************************************************************************************************

#*********************************************curd cheese**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="curd cheese"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\curd cheese.csv", sep = ",")
#************************************************************************************************

#*********************************************decalcifier**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="decalcifier"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\decalcifier.csv", sep = ",")
#************************************************************************************************

#*********************************************dental care**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="dental care"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\dental care.csv", sep = ",")
#************************************************************************************************

#*********************************************ddessert**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="dessert"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\dessert.csv", sep = ",")
#************************************************************************************************

#*********************************************detergent**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="detergent"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\detergent.csv", sep = ",")
#************************************************************************************************

#*********************************************dish cleaner**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="dish cleaner"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\dish cleaner.csv", sep = ",")
#************************************************************************************************

#*********************************************dishesr**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="dishes"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\dishes.csv", sep = ",")
#************************************************************************************************

#*********************************************dog food**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="dog food"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\dog food.csv", sep = ",")
#************************************************************************************************

#*********************************************domestic eggs**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="domestic eggs"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\domestic eggs.csv", sep = ",")
#************************************************************************************************

#*********************************************female sanitary products**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="female sanitary products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\female sanitary products.csv", sep = ",")
#************************************************************************************************

#*********************************************finished products**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="finished products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\finished products.csv", sep = ",")
#************************************************************************************************

#*********************************************fish**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="fish"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\fish.csv", sep = ",")
#************************************************************************************************

#*********************************************flour**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="flour"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\flour.csv", sep = ",")
#************************************************************************************************

#*********************************************flower (seeds)**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="flower (seeds)"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\flower (seeds).csv", sep = ",")
#************************************************************************************************

#*********************************************flower soil/fertilizer**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="flower soil/fertilizer"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\flowersoilfertilizer.csv", sep = ",")
#************************************************************************************************

#*********************************************frankfurter**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frankfurter"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frankfurter.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen chicken**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen chicken"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen chicken.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen dessert**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen dessert"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen dessert.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen fish**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen fish"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen fish.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen fruits**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen fruits"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen fruits.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen meals**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen meals"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen meals.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen potato products**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen potato products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen potato products.csv", sep = ",")
#************************************************************************************************

#*********************************************frozen vegetables**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="frozen vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\frozen vegetables.csv", sep = ",")
#************************************************************************************************

#*********************************************fruit/vegetable juice**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="fruit/vegetable juice"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\fruitvegetable juice.csv", sep = ",")
#************************************************************************************************

#*********************************************grapes**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="grapes"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\grapes.csv", sep = ",")
#************************************************************************************************

#*********************************************hair spray**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="hair spray"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\hair spray.csv", sep = ",")
#************************************************************************************************

#*********************************************ham**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="ham"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\ham.csv", sep = ",")
#************************************************************************************************

#*********************************************hamburger meat**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="hamburger meat"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\hamburger meat.csv", sep = ",")
#************************************************************************************************

#********************************************hard cheese**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="hard cheese"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\hard cheese.csv", sep = ",")
#************************************************************************************************

#********************************************herbs**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="herbs"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\herbs.csv", sep = ",")
#************************************************************************************************

#********************************************honey**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="honey"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\honey.csv", sep = ",")
#************************************************************************************************

#********************************************honey**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="honey"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\honey.csv", sep = ",")
#************************************************************************************************

#********************************************house keeping products**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="house keeping products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\house keeping products.csv", sep = ",")
#************************************************************************************************

#********************************************hygiene articles**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="hygiene articles"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\hygiene articles.csv", sep = ",")
#************************************************************************************************

#********************************************ice cream**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="ice cream"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\ice cream.csv", sep = ",")
#************************************************************************************************

#********************************************instant coffee**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="instant coffee"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\instant coffee.csv", sep = ",")
#************************************************************************************************

#********************************************ijam**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="jam"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\jam.csv", sep = ",")
#************************************************************************************************

#********************************************ketchup**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="ketchup"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\ketchup.csv", sep = ",")
#************************************************************************************************

#********************************************ketchup**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="ketchup"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\ketchup.csv", sep = ",")
#************************************************************************************************

#********************************************kitchen towels**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="kitchen towels"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\kitchen towels.csv", sep = ",")
#************************************************************************************************

#********************************************kitchen utensils**************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="kitchen utensil"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\kitchen utensil.csv", sep = ",")
#************************************************************************************************

#*******************************************light bulbs*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="light bulbs"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\light bulbs.csv", sep = ",")
#************************************************************************************************

#*******************************************liqueur*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="liqueur"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\liqueur.csv", sep = ",")
#************************************************************************************************

#*******************************************liquor*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="liquor"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\liquor.csv", sep = ",")
#************************************************************************************************

#*******************************************liquor (appetizer)*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="liquor (appetizer)"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\liquor (appetizer).csv", sep = ",")
#************************************************************************************************

#*******************************************liver loaf*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="liver loaf"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\liver loaf.csv", sep = ",")
#************************************************************************************************

#******************************************long life bakery product*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="long life bakery product"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\long life bakery product.csv", sep = ",")
#************************************************************************************************

#******************************************make up remover*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="make up remover"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\make up remover.csv", sep = ",")
#************************************************************************************************

#******************************************male cosmetics*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="male cosmetics"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\male cosmetics.csv", sep = ",")
#************************************************************************************************

#******************************************margarine*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="margarine"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\margarine.csv", sep = ",")
#************************************************************************************************

#******************************************mayonnaise*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="mayonnaise"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\mayonnaise.csv", sep = ",")
#************************************************************************************************


#******************************************meat*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="meat"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\meat.csv", sep = ",")
#************************************************************************************************

#******************************************misc. beverages*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="misc. beverages"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\miscbeverages.csv", sep = ",")
#************************************************************************************************

#*****************************************mustard************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="mustard"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\mustard.csv", sep = ",")
#************************************************************************************************

#*****************************************napkins************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="napkins"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\napkins.csv", sep = ",")
#************************************************************************************************

#*****************************************newspapers************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="newspapers"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\newspapers.csv", sep = ",")
#************************************************************************************************

#*****************************************nut snack************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="nut snack"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\nut snack.csv", sep = ",")
#************************************************************************************************

#****************************************nuts/prunes************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="nuts/prunes"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\nutsprunes.csv", sep = ",")
#************************************************************************************************

#****************************************oil***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="oil"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\oil.csv", sep = ",")
#************************************************************************************************

#****************************************onions***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="onions"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\onions.csv", sep = ",")
#************************************************************************************************

#****************************************organic products***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="organic products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\organic products.csv", sep = ",")
#************************************************************************************************

#****************************************organic sausages***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="organic sausage"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\organic sausage.csv", sep = ",")
#************************************************************************************************

#***************************************other vegetables***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="other vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\other vegetables.csv", sep = ",")
#************************************************************************************************

#***************************************packaged fruit/vegetabless***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="packaged fruit/vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\packaged fruitvegetables.csv", sep = ",")
#************************************************************************************************

#***************************************pasta***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pasta"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pasta.csv", sep = ",")
#************************************************************************************************

#***************************************pastry***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pastry"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pastry.csv", sep = ",")
#************************************************************************************************

#***************************************pet care***********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pet care"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pet care.csv", sep = ",")
#***********************************************************************************************

#***************************************photo/film********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="photo/film"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\photofilm.csv", sep = ",")
#***********************************************************************************************


#**************************************pickled vegetables****************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pickled vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pickled vegetables.csv", sep = ",")
#***********************************************************************************************

#**************************************pip fruit***************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pip fruit"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pip fruit.csv", sep = ",")
#***********************************************************************************************

#**************************************ppopcorn*************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="popcorn"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\popcorn.csv", sep = ",")
#***********************************************************************************************


#**************************************pork*************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pork"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pork.csv", sep = ",")
#***********************************************************************************************

#**************************************pot plants*************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pot plants"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pot plants.csv", sep = ",")
#***********************************************************************************************


#**************************************potato products*************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="potato products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\potato products.csv", sep = ",")
#***********************************************************************************************

#**************************************preservation products***********************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="preservation products"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\preservation products.csv", sep = ",")
#***********************************************************************************************

#**************************************processed cheese*********************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="processed cheese"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\processed cheese.csv", sep = ",")
#***********************************************************************************************

#**************************************prosecco*********************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="prosecco"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\prosecco.csv", sep = ",")
#***********************************************************************************************

#***************************************************pudding powder*************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="pudding powder"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\pudding powder.csv", sep = ",")
#***********************************************************************************************

#***************************************************ready soups************************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="ready soups"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\ready soups.csv", sep = ",")
#***********************************************************************************************

#**************************************************red/blush wine**********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="red/blush wine"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\redblush wine.csv", sep = ",")
#***********************************************************************************************

#**************************************************rice*********************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="rice"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\rice.csv", sep = ",")
#***********************************************************************************************

#**************************************************roll products *********************************************
#print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
#rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
#              appearance = list(default="rhs",lhs="roll products"),
#              control = list(verbose=F))

#reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
#write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\roll products.csv", sep = ",")
#***********************************************************************************************

#*************************************************rolls/buns****************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="rolls/buns"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\rollsbuns.csv", sep = ",")
#***********************************************************************************************

#*************************************************root vegetables**************************************
print("Commencing Specialized association rule mining for -  abrasive cleaner - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="root vegetables"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_PARAMETERIZED_ARM script\\root vegetables.csv", sep = ",")
#***********************************************************************************************



































print("Prining Specialized association rule mining for -  whole milk - MINIMUM LENGTH OF RULE = 2")
print(inspect(reresorted[1:5]))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

library(arulesViz)
#png("D:\\FYP\\R\\mba\\wholemilk.png", width=4, height=4, units="in", res=300)
plot(reresorted,method="graph",interactive=TRUE,shading=NA)
dev.off()


