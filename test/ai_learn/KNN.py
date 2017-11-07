

from numpy import *
import operator
def createDateSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    print(distances)
    sortedDistances = distances.argsort()
    classCount = {}
    print(sortedDistances)
    for i in range(k):
        votelabel = labels[sortedDistances[i]]
        print(votelabel)
        classCount[votelabel]=classCount.get(votelabel,0) + 1
        print(classCount)
    print(classCount)
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

if __name__ == "__main__":
    group,labels = createDateSet()
    result = classify0([0,0],group,labels,3)
    print(result)