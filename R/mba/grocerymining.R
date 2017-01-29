#Loading data
library(arules)
library(arulesViz)
library(datasets)

#load data set groceries 
data(Groceries)

#create frequency list
#itemFrequencyPlot(Groceries,topN=20,type="absolute")

#fit <- lm(itemFrequencyPlot(Groceries,topN=20,type="absolute"))

#png(filename="D:\\plot.png")
#plot(fit)
#dev.off()

ry <- apriori(Groceries,parameter = list(supp = 0.001,conf = 0.8))

#show em
options(digits = 2)
print('Printing Basic assocation rules')
print(inspect(ry[1:5]))
print("/n")
print("/n")


#apassata kiyawapan 
print("========================")
roy <- sort(ry,by="confidence",decreasing = TRUE)
print("Printing sorted association rules according to confidence level")
print(roy)
print("/n")
print("/n")


#print("aiyooooooooooooooooooo")
print(",.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")
options(digits = 2)
print("Printing for two digits of the sorted set")
print(inspect(roy[1:35]))
print(",.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")

#============================================
fileConn<-file("D:\\R\\mba\\FW.txt")
fileConn2<-file("D:\\R\\mba\\Output.txt")
writeLines(c("Hello","World"), fileConn)

print("/n")
print("/n")
print("Commencing file writing off all association rules")

write(roy, file = "D:\\FYP\\R\\mba\\newdata.csv", sep = ",")


close(fileConn)
print("/n")
print("/n")

#==================================

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

