print("BEGIN")

# Load necessary libraries
library(datasets)

# Inspect data structure
print(str(attitude))

print(summary(attitude))

# Subset the attitude data
dat = attitude[,c(3,4)]

# Plot subset data
plot(dat, main = "% of favourable responses to
     Learning and Privilege", pch =20, cex =2)

#  kmeans 2 clusters 
set.seed(7)
km1 = kmeans(dat, 3, nstart=100)

# Plot results
plot(dat, col =(km1$cluster +1) , main="K-Means result with 2 clusters", pch=20, cex=2)


mydata <- dat
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)

print(wss)
plot(1:15, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method",
     pch=20, cex=2)

# 6 
km6 = kmeans(dat, 6, nstart=100)
plot(dat, col =(km6$cluster +1) , main="K-Means result with 6 clusters", pch=20, cex=2)
print(km6)
print(km6$cluster)


print(km6$cluster==1)

print(km6$cluster==2)
print(km6$cluster==3)
print(km6$cluster==4)
print(km6$cluster==5)
print(km6$cluster==6)
