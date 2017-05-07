#Loading data
library(arules)
library(arulesViz)
library(datasets)

#load data set groceries 
#p <- data(Groceries)
#View(p)
#create frequency list
#itemFrequencyPlot(Groceries,topN=20,type="absolute")

#fit <- lm(itemFrequencyPlot(Groceries,topN=20,type="absolute"))

#png(filename="D:\\plot.png")
#plot(fit)
#dev.off()
#View(data("Groceries"))

ry <- apriori(Groceries,parameter = list(supp = 0.001,conf = 1))
print(length(ry))
print(" p po po po po po po po po po po po po ")
print(system.time(apriori(Groceries,parameter = list(supp = 0.001,conf = 1))))
print(" uiiuiuiiu iu iu iu iu iui ui ")
