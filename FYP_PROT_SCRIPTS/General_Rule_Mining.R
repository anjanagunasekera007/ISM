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



#apassata kiyawapan 
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
options(digits = 2)
roy <- sort(ry,by="confidence",decreasing = TRUE)
print("Printing sorted association rules according to confidence level")
print(inspect(roy))
print("/n")
print("/n")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")

#============================================
print("========== WRITING ============")
#fileConn<-file("D:\\FYP\\FYP_PROT_SCRIPTS\\FW.txt")
#fileConn2<-file("D:\\FYP\\FYP_PROT_SCRIPTS\\FW.txt")
#writeLines(c("Hello","World"), fileConn)

print("/n")
print("/n")
print("Commencing file writing off all association rules")

write(roy, file = "D:\\FYP\\FYP_PROT_SCRIPTS\\FW.txt", sep = ",")


#close(fileConn)
print("/n")
print("/n")

print("========== COMPLETED ============")


#==================================