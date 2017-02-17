print("BEGIN")

# Load necessary libraries
library(datasets)

# Inspect data structure
print(str(attitude))

print(summary(attitude))

# Subset the attitude data
dat = attitude[,c(3,4)]

print("Printing subsetted data")
print(dat)

# Plot subset data
plot(dat, main = "% of favourable responses to
     Learning and Privilege", pch =20, cex =2)

#Kmens with 2 clusters 
#elbow curve not yet 
# Perform K-Means with 2 clusters
set.seed(7)
km1 = kmeans(dat, 2, nstart=100)

# Plot results
plot(dat, col =(km1$cluster +1) , main="K-Means result with 2 clusters", pch=20, cex=2)

mydata <- dat
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)

plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Plotting the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)

#identified number of clusters
set.seed(7)
km2 = kmeans(dat, 6, nstart=100)

# Examine the result of the clustering algorithm
print(km2)
print("completed")

plot(dat, col =(km2$cluster +1) , main="K-Means result with 6 clusters", pch=20, cex=2)
