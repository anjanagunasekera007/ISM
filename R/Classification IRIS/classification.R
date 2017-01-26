iris <- read.csv(url("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"), header = FALSE)

names(iris) <- c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species")

library(ggvis)

view_static(iris %>% ggvis(~Sepal.Length,~Sepal.Width,fill=~Species) %>% layer_points())

view_static(iris %>% ggvis(~Petal.Length, ~Petal.Width, fill = ~Species) %>% layer_points())

table(iris$Species)
round(prop.table(table(iris$Species))*100,digits = 1)

#rrr
print(summary(iris))

library(class)

normalize <- function(x){
  num <- x - min(x)
  denom <- max(x) - min(x)
  return (num/denom)
}

iris_norm <- as.data.frame(lapply(iris[1:4], normalize))
print(summary(iris_norm))


set.seed(1234)
ind <- sample(2, nrow(iris), replace=TRUE, prob=c(0.67, 0.33))

iris.training <- iris[ind==1,1:4]
iris.test <- iris[ind==2,1:4]

iris.trainLabels <- iris[ind==1, 5]
iris.testLabels <- iris[ind==2, 5]


print(summary(iris.training))
print("-------------------")
print(iris.test)
print( " KNN UNDER TRAINING")
iris_pred <- knn(train = iris.training, test = iris.test, cl = iris.trainLabels, k=3)

print( " KNN TRAIN COMPLETED ")

print("TEST LABLES ")
library(gmodels)
print("library loaded")
CrossTable(x = iris.testLabels, y = iris_pred, prop.chisq=FALSE)



