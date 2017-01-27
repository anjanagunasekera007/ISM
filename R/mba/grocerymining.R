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
print(inspect(ry[1:5]))
#apassata kiyawapan 
print("========================")
roy <- sort(ry,by="confidence",decreasing = TRUE)
print(roy)
#print("aiyooooooooooooooooooo")
print(",.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")
options(digits = 2)
print(inspect(roy[1:35]))
print(",.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,.,")

#============================================
fileConn<-file("D:\\R\\mba\\FW.txt")
fileConn2<-file("D:\\R\\mba\\Output.txt")
writeLines(c("Hello","World"), fileConn)

write(roy, file = "D:\\FYP\\R\\mba\\newdata.csv", sep = ",")


close(fileConn)

#==================================

#filter =3 lift none max value 11.5 
#rules <- apriori(Groceries,parameter = list(support=0.001,conf=0.8, maxlen=3))

rah<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.08), 
               appearance = list(default="lhs",rhs="whole milk"),
               control = list(verbose=F))

rah<-sort(rah, decreasing=TRUE,by="confidence")

print(inspect(rah[1:5]))

#print(rah)
#sortedrah < -sort(rah, decreasing=TRUE,by="confidence")

print("--------------------------------")
#print(inspect(sortedrah[1:5]))


rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
               appearance = list(default="rhs",lhs="yogurt"),
               control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

print(inspect(reresorted[1:5]))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

library(arulesViz)
plot(reresorted,method="graph",interactive=TRUE,shading=NA)

