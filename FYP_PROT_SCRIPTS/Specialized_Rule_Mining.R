#filter =3 lift none max value 11.5 
#rules <- apriori(Groceries,parameter = list(support=0.001,conf=0.8, maxlen=3))
print("Commencing Specialized association rule mining for -  whole milk - ")
rah<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.08), 
             appearance = list(default="lhs",rhs="whole milk"),
             control = list(verbose=F))

rah<-sort(rah, decreasing=TRUE,by="confidence")
print("Prining Specialized association rule mining for -  whole milk - ")
print(inspect(rah[1:5]))

#print(rah)
#sortedrah < -sort(rah, decreasing=TRUE,by="confidence")

#print("--------------------------------")
#print(inspect(sortedrah[1:5]))

print("Commencing Specialized association rule mining for -  whole milk - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="whole milk"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

print("Prining Specialized association rule mining for -  whole milk - MINIMUM LENGTH OF RULE = 2")
print(inspect(reresorted[1:5]))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

library(arulesViz)
plot(reresorted,method="graph",interactive=TRUE,shading=NA)

