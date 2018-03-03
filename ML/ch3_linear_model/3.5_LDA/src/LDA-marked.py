from _operator import inv
'''
data importion and pre-analysis
'''
import numpy as np  # for matrix calculation
import matplotlib.pyplot as plt 

# load the CSV file as a numpy matrix
data_file = open('../data/watermelon_3a.csv')
dataset = np.loadtxt(data_file, delimiter=",")

# separate the data from the target attributes
X = dataset[:,1:3]  #第[1-3)列 不包含第3列
y = dataset[:,3]    #第3列

# draw scatter diagram to show the raw data
f1 = plt.figure(1)       
plt.title('watermelon_3a')  
plt.xlabel('density')  
plt.ylabel('ratio_sugar')  
plt.scatter(X[y == 0,0], X[y == 0,1], marker = 'o', color = 'k', s=100, label = 'bad')  #当s是同x大小的数组，表示x中的每个点对应s中一个大小，默认20
# y = 0 的第0列和第1列
plt.scatter(X[y == 1,0], X[y == 1,1], marker = 'o', color = 'g', s=100, label = 'good')
# y = 1 的第0列和第1列
plt.legend(loc = 'upper right')  



# 1-st. get the mean vector of each class

u = []  
for i in range(2): # two class
    u.append(np.mean(X[y==i], axis=0))  # column mean y = 0; y = 1 are the two classes ; calculate the mean of the two columns when y = i(0 / 1) 

# 2-nd. computing the within-class scatter matrix, refer on book (3.33)
m,n = np.shape(X)
Sw = np.zeros((n,n))
for i in range(m):
    x_tmp = X[i].reshape(n,1)  # row -> cloumn vector
    if y[i] == 0: u_tmp = u[0].reshape(n,1)
    if y[i] == 1: u_tmp = u[1].reshape(n,1)
    Sw += np.dot( x_tmp - u_tmp, (x_tmp - u_tmp).T )  # np.dot : multi the matrixs

Sw = np.mat(Sw)
U, sigma, V= np.linalg.svd(Sw) #SVD奇异值分解 这里sigma只是奇异值数组，不是对角矩阵：sigma = [a,b]; np.diag(sigma) = [[a,0],[0,b]]

Sw_inv = V.T * np.linalg.inv(np.diag(sigma)) * U.T

# 3-th. computing the parameter w, refer on book (3.39)
w = np.dot( Sw_inv, (u[0] - u[1]).reshape(n,1) )  # here we use a**-1 to get the inverse of a ndarray

print(w)  #get the result w

f3 = plt.figure(3)
plt.xlim( -0.2, 1 )  # x轴坐标范围
plt.ylim( -0.5, 0.7 )

p0_x0 = -X[:, 0].max()  #第0列最大值取反
#w: [[-6.62487509e-04]
#    [-9.36728168e-01]]
#是一个vector, 故w[1, 0] = -9.36728168e-01
p0_x1 = ( w[1,0] / w[0,0] ) * p0_x0  # w[1,0] / w[0,0]为斜率
p1_x0 = X[:, 0].max()
p1_x1 = ( w[1,0] / w[0,0] ) * p1_x0
p1_x1 = ( w[1,0] / w[0,0] ) * p1_x0

plt.title('watermelon_3a - LDA')  
plt.xlabel('density')  
plt.ylabel('ratio_sugar')  
plt.scatter(X[y == 0,0], X[y == 0,1], marker = 'o', color = 'k', s=10, label = 'bad')
plt.scatter(X[y == 1,0], X[y == 1,1], marker = 'o', color = 'g', s=10, label = 'good')
plt.legend(loc = 'upper right')  

plt.plot([p0_x0, p1_x0], [p0_x1, p1_x1])  #打印投影线

# draw projective point on the line
from self_def import GetProjectivePoint_2D 

m,n = np.shape(X)
for i in range(m):
    x_p = GetProjectivePoint_2D( [X[i,0], X[i,1]], [w[1,0] / w[0,0] , 0] ) 
    if y[i] == 0: 
        plt.plot(x_p[0], x_p[1], 'ko', markersize = 5)
    if y[i] == 1: 
        plt.plot(x_p[0], x_p[1], 'go', markersize = 5)   
    plt.plot([ x_p[0], X[i,0]], [x_p[1], X[i,1] ], 'c--', linewidth = 0.3)

'''
implementation of LDA again after delete outlier (X[14])
'''
# computing the d-dimensional mean vectors
# import numpy as np

# 1-st. get the mean vector of each class
X = np.delete(X, 14, 0)
y = np.delete(y, 14, 0)

#过程同3
u = []  
for i in range(2): # two class
    u.append(np.mean(X[y==i], axis=0))  # column mean

# 2-nd. computing the within-class scatter matrix, refer on book (3.33)
m,n = np.shape(X)
Sw = np.zeros((n,n))
for i in range(m):
    x_tmp = X[i].reshape(n,1)  # row -> cloumn vector
    if y[i] == 0: u_tmp = u[0].reshape(n,1)
    if y[i] == 1: u_tmp = u[1].reshape(n,1)
    Sw += np.dot( x_tmp - u_tmp, (x_tmp - u_tmp).T )

Sw = np.mat(Sw)
U, sigma, V= np.linalg.svd(Sw) 

Sw_inv = V.T * np.linalg.inv(np.diag(sigma)) * U.T
# 3-th. computing the parameter w, refer on book (3.39)
w = np.dot( Sw_inv, (u[0] - u[1]).reshape(n,1) )  # here we use a**-1 to get the inverse of a ndarray

print(w)

# 4-th draw the LDA line in scatter figure

# f2 = plt.figure(2)
f4 = plt.figure(4)
plt.xlim( -0.2, 1 )
plt.ylim( -0.5, 0.7 )

p0_x0 = -X[:, 0].max()
p0_x1 = ( w[1,0] / w[0,0] ) * p0_x0
p1_x0 = X[:, 0].max()
p1_x1 = ( w[1,0] / w[0,0] ) * p1_x0

plt.title('watermelon_3a - LDA')  
plt.xlabel('density')  
plt.ylabel('ratio_sugar')  
plt.scatter(X[y == 0,0], X[y == 0,1], marker = 'o', color = 'k', s=10, label = 'bad')
plt.scatter(X[y == 1,0], X[y == 1,1], marker = 'o', color = 'g', s=10, label = 'good')
plt.legend(loc = 'upper right')  

plt.plot([p0_x0, p1_x0], [p0_x1, p1_x1])

# draw projective point on the line
from self_def import GetProjectivePoint_2D 

m,n = np.shape(X)
for i in range(m):
    x_p = GetProjectivePoint_2D( [X[i,0], X[i,1]], [w[1,0] / w[0,0] , 0] ) 
    if y[i] == 0: 
        plt.plot(x_p[0], x_p[1], 'ko', markersize = 5)
    if y[i] == 1: 
        plt.plot(x_p[0], x_p[1], 'go', markersize = 5)   
    plt.plot([ x_p[0], X[i,0]], [x_p[1], X[i,1] ], 'c--', linewidth = 0.3)

plt.show()