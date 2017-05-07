print("BEGIN")

# Load necessary libraries
library(datasets)

mydata = read.csv("D:\\FYP\\R\\FINAL_CLUSTERING_SCRIPT\\customerdata.csv")  # read csv file 

View(mydata)

print(summary(mydata))


dat = mydata[,c(1,2)]

print(dat)

plot(dat, main = "% Age vs Distance
     ", pch =20, cex =2)

#set.seed(7)
#km1 = kmeans(dat, 2, nstart=100)

# Plot results
#plot(dat, col =(km1$cluster +1) , main="K-Means result with 2 clusters", pch=20, cex=2)

#elbowwwww :P :P 
mydata <- dat
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)


plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Plotting the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)


#identified number of clusters
set.seed(12)
km2 = kmeans(dat, 9, nstart=100)

# Examine the result of the clustering algorithm
print(km2)
print("completed")

plot(dat, col =(km2$cluster +1) , main="K-Means result with 9 clusters", pch=20, cex=2)




#============================================
#fileConn<-file("D:\\R\\ATTITUDE_EXAMPLE\\clusters1.txt")
#fileConn2<-file("D:\\R\\ATTITUDE_EXAMPLE\\clusters2.txt")
#writeLines(c("Hello","World"), fileConn)

print("/n")
print("/n")
print("Commencing file writing of all clusters")

write(km2$cluster, file = "D:\\FYP\\R\\FINAL_CLUSTERING_SCRIPT\\clusters.txt", sep = ",")


close(fileConn)
print("/n")
print("/n")

#==================================

print(nrow(dat))
#print(km2$cluster)


