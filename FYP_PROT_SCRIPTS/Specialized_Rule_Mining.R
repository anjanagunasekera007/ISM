#Loading data
library(arules)
library(arulesViz)
library(datasets)

#load data set groceries 
data(Groceries)

item1 <- "whole milk"
item2 <- "butter"
#filter =3 lift none max value 11.5 
#rules <- apriori(Groceries,parameter = list(support=0.001,conf=0.8, maxlen=3))
print("Commencing Specialized association rule mining for -  whole milk - ")
wholemilk<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.08), 
             appearance = list(default="lhs",rhs=item1),
             control = list(verbose=F))

butter<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.08), 
             appearance = list(default="lhs",rhs=item2),
             control = list(verbose=F))

wholemilk_sorted<-sort(wholemilk, decreasing=TRUE,by="confidence")
butter_sorted<-sort(butter, decreasing=TRUE,by="confidence")


print("Prining Specialized association rule mining for -  whole milk - ")
print(inspect(wholemilk_sorted[1:5]))
print("*****************************************************************************")
print("Prining Specialized association rule mining for -  Butter - ")
print(inspect(butter_sorted[1:5]))


print("========== WRITING ============")

print("/n")
print("/n")
print("Commencing file writing of whole milk")

write(wholemilk_sorted, file = "D:\\FYP\\FYP_PROT_SCRIPTS\\WHOLE_MILK.txt", sep = ",")

print("/n")
print("/n")

print("========== COMPLETED ============")



print("========== WRITING ============")

print("/n")
print("/n")
print("Commencing file writing of whole milk")

write(butter_sorted, file = "D:\\FYP\\FYP_PROT_SCRIPTS\\BUTTER.txt", sep = ",")

print("/n")
print("/n")

print("========== COMPLETED ============")

