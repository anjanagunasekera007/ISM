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
#fileConn<-file("D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\FW.txt")
#fileConn2<-file("D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\Output.txt")
#writeLines(c("Hello","World"), fileConn)

print("/n")
print("/n")
print("Commencing file writing off all association rules")

write(roy, file = "D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\association_rules.csv", sep = ",")


#close(fileConn)
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

#************************************************************************************************************************
print("Commencing Specialized association rule mining for -  whole milk - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
               appearance = list(default="rhs",lhs="whole milk"),
               control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\whole_milk.csv", sep = ",")

#*************************************************************************************************************************
print("Commencing Specialized association rule mining for -  Brown bread - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="brown bread"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\brown_bread.csv", sep = ",")
#*************************************************************************************************************************

#*************************************************************************************************************************
print("Commencing Specialized association rule mining for -  beef - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="beef"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\beef.csv", sep = ",")
#*************************************************************************************************************************

#*************************************************************************************************************************
print("Commencing Specialized association rule mining for -  chicken - MINIMUM LENGTH OF RULE = 2")
rere<-apriori(data=Groceries, parameter=list(supp=0.001,conf = 0.15,minlen=2), 
              appearance = list(default="rhs",lhs="chicken"),
              control = list(verbose=F))

reresorted<-sort(rere, decreasing=TRUE,by="confidence")

#Write Association rules with whole milk as LHS 
write(reresorted, file = "D:\\FYP\\R\\FINAL_RULE_MINING_SCRIPT\\chicken.csv", sep = ",")
#*************************************************************************************************************************






print("Prining Specialized association rule mining for -  whole milk - MINIMUM LENGTH OF RULE = 2")
print(inspect(reresorted[1:5]))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

library(arulesViz)
png("D:\\FYP\\R\\mba\\wholemilk.png", width=4, height=4, units="in", res=300)
plot(reresorted,method="graph",interactive=TRUE,shading=NA)
dev.off()


#==============

#x <- rnorm(1000000)
#y <- rnorm(1000000)

#png("D:\\FYP\\R\\mba\\myplot.png", width=4, height=4, units="in", res=300)
#par(mar=c(4,4,1,1))
#plot(x,y,col=rgb(0,0,0,0.03), pch=".", cex=2)
#dev.off()

#==============



