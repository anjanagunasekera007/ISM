print("Beginning customer segementation with data file")

mydata = read.csv("D:\\FYP\\R\\customer segmentation\\Reconfigured.csv") 

View(mydata)

print(summary(mydata))

dat = mydata[,c(1,2)]

print(dat)

plot(dat, main = "% of favourable responses to
     distance and agegroup", pch =20, cex =2)

set.seed(7)
km1 = kmeans(dat, 3, nstart=100)

plot(dat, col =(km1$cluster +1) , main="K-Means result with 2 clusters", pch=20, cex=2)

print(wss)
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)

km6 = kmeans(dat, 8, nstart=100)
plot(dat, col =(km6$cluster +1) , main="K-Means result with 6 clusters", pch=20, cex=2)
print(km6)
print(km6$cluster)