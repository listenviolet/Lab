import numpy as np 
import matplotlib.pyplot as plt 
def loadDataSet():
	dataMat = []; labelMat = []
	with open('logisticData.txt') as f:
		for line in f.readlines():
			lineList = line.strip().split()
			dataMat.append([1.0, float(lineList[0]), float(lineList[1])])
			labelMat.append(int(lineList[2]))
	return dataMat, labelMat

def sigmoid(z):
	return 1.0 / (1 + np.exp(-z))

def impovedStoGradAscent(dataMat, labelMat, numInter = 150):
	dataMatrix = np.mat(dataMat)
	n, m = np.shape(dataMatrix)
	weights = np.mat(np.ones((m, 1)))
	for j in range(numInter):
		dataIndex = list(range(n))
		for i in range(n):
			alpha = 2 / (1.0 + j + i) + 0.0001
			randIndex = int(np.random.uniform(0,len(dataIndex)))
			predictlabel = sigmoid(dataMatrix[randIndex] * weights)
			error = labelMat[randIndex] - predictlabel
			gradient = np.multiply(dataMatrix[randIndex], error)
			weights = weights + alpha * gradient.transpose()

			del dataIndex[randIndex]
	return weights

def plotDataSet(dataMat):
	x1 = np.mat(dataMat)[:,1] # the 1st column
	x2 = np.mat(dataMat)[:,2] # the 2ed column
	line1,= plt.plot(x1[:50], x2[:50], 'ro', label = 'class1')
	line2,= plt.plot(x1[50:], x2[50:], 'b^', label = 'class0')
	plt.xlabel('x1')
	plt.ylabel('x2')
	plt.legend(handles = [line1, line2], loc = 2) 

def plotBestFit(dataMat, weights):
	plt.figure()
	plotDataSet(dataMat)
	x = np.mat(np.arange(-4.0, 4.0, 0.1))
	y = (-weights[0] - weights[1] * x) / weights[2]
	plt.plot(x.transpose(), y.transpose())  #draw the line
	plt.show()

def logisticTest(weights, testData):
	n, m =np.shape(np.mat(testData))
	testLable = np.zeros((n,1))
	for i in range(n):
		testLable[i] = weights[0] + weights[1] * testData[i][0] + weights[2] * testData[i][1]
		if testLable[i] >= 0.5 : testLable[i] = 1
	else: testLable[i] = 0
	return testLable

if __name__ == '__main__':
	dataMat, labelMat = loadDataSet()
	weights = impovedStoGradAscent(dataMat, labelMat, numInter = 150)
	plotBestFit(dataMat, weights)
	testLable = logisticTest(weights, [[0,0],[0,10]])
	#print(testLable[0])