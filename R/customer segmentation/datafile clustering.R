print("Beginning customer segementation with data file")

mydata = read.csv("D:\\FYP_DATA\\JAVA\\DATA_GENERATION_RECONFIGURATION\\Reconfigured_Data_Customers_Items.csv") 

View(mydata)

print(summary(mydata))

dat = mydata[,c(1,2)]

print(dat)

plot(mydata, main = "% of favourable responses to
     distance and agegroup", pch =20, cex =2)

set.seed(7)
km1 = kmeans(mydata, 8, nstart=100)

plot(mydata, col =(km1$cluster +1) , main="K-Means result with 2 clusters", pch=20, cex=2)

print(wss)
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)

km6 = kmeans(mydata, 8, nstart=100)
plot(mydata, col =(km6$cluster +1) , main="K-Means result with 6 clusters", pch=20, cex=2)
print(km6)
print(km6$cluster)