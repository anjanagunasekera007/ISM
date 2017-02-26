#setdir
library(dummies)

path <- "D:\\FYP\\R\\PCA"

#setpwd
setwd(path)

#loaddata
train <-read.csv("D:\\FYP\\R\\PCA\\Train_Big.csv")
test <- read.csv("D:\\FYP\\R\\PCA\\Test_Big.csv")

#addacoloumnssa
test$Item_Outlet_Sales <- 1

#cmb
combi <- rbind(train,test)

#imputemissingvalues with mediana
combi$Item_Weight[is.na(combi$Item_Weight)] <- median(combi$Item_Weight, na.rm = TRUE)

#find mode and impute
table(combi$Outlet_Size, combi$Outlet_Type)
levels(combi$Outlet_Size)[1] <- "Other"

#remove dependencies
my_data <- subset(combi, select = -c(Item_Outlet_Sales, Item_Identifier,Outlet_Identifier))

#check
print(colnames(my_data))

print("-----")
print(str(my_data))

#make frames
new_my_data <- dummy.data.frame(my_data,names = )



