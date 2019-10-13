from numpy import *
import service.cluster.kmeans.kmeans as kmeans

## step 1: load data
print("step 1: load data...")
dataSet = []
fileIn = open('./testSet.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(' ')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering...
print("step 2: clustering...")
dataSet = mat(dataSet)
k = 4
centroids, clusterAssment = kmeans.kmeans(dataSet, k)

## step 3: show the result
print("step 3: show the result...")
kmeans.showCluster(dataSet, k, centroids, clusterAssment)

