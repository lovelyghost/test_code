# -*- coding:utf-8 -*-
import numpy as np

h = np.array([[1,2,3],[2,3,4]],dtype=complex) # 创建数组
print(h)
print(h.shape) # 查看维度
print(h.size) # 查看数组元素个数
print(h.dtype)  # 查看数组元素数据类型
print(np.zeros((3,3))) # 生成二维元组为0数组 ,默认数组类型float64
print(np.ones((3,3))) # 生成二维元组为1数组, ,默认数组类型float64

print(np.arange(0,100,5)) # 按步长5,生成0-100 一维数组, ,默认数组类型float64

print(np.arange(0,100).reshape(10,10)) # 10行10列,生成0-100 二维数组, ,默认数组类型float64

print(np.linspace(0,100,11)) # 从0到100按数组长度10个生成数组,默认数组类型float64

print(np.random.random((3,3))) # 随机数填充数组,3行3列

# numpy 运算 元素级加法,减法,乘法,正弦等等
a = np.arange(4)
b = np.arange(4)
print(a+b)
print(a*2)
print(a-2)
print(a-b)
print(np.sin(a))

# 矩阵积
A = np.arange(0,9).reshape((3,3))
B = np.ones((3,3))
print(np.dot(A,B))
print(A.dot(B))

# 数组自增自减运算
C = np.arange(4)
C+=5
print(C)
C-=3
print(C)

# 通用函数
D = np.arange(10,30)
print(np.sqrt(D))
print(np.log(D))
print(np.sin(D))

# 聚合函数
print(np.sum(D))
print(np.min(D))
print(np.mean(D))

# 索引
# 一维数组
print(D[3])
print(D[-2])
print(D[[3,5]])

# 二维数组索引
E = np.arange(10,19).reshape((3,3))
print(E)
print(E[1,2]) # 2行3列
print(E[0,2]) # 1行3列

# 切片操作
# 一维
F = np.arange(10,19)
print(F[2:4])
print(F[2:9:3]) #隔3个取一个值

# 二维
G = np.arange(10,19).reshape((3,3))
print(G)
print(G[0,:]) # 取第一行,:冒号表示所有列
print(G[:,0]) # 取第一列,:冒号表示所有行
print(G[0:2,0:2]) # 取1,2列,取1,2行

# 数组迭代

# 按行迭代
for i in G:
    print(i)
# 遍历每一个元素
for i in G.flat:
    print(i)
# 纯 numpy处理循环
print(np.apply_along_axis(np.mean,axis=0,arr=G)) # axis=0按行求平均值
print(np.apply_along_axis(np.mean,axis=1,arr=G)) # axis=1按列求平均值

# 元素级函数处理
def dd(x):
    return x/2
print(np.apply_along_axis(dd,axis=1,arr=G)) # axis=1按列折半

# 条件和布尔数组

H = np.random.random((5,5))
print(H)
print(H>0.5)
print(H[H>0.5]) # 获取组成的新数组

# 数组形状变换
print(H.reshape(5,5))
print(H.transpose()) # 矩阵转置
print(H.ravel())  # 重新变成一维数组

# 连接数组
I = np.ones((3,3))
J = np.zeros((3,3))
print(I)
print(J)
print(np.vstack((I,J))) # 垂直入栈
print(np.hstack((I,J))) # 水平入栈
print("连接操作")
print(np.concatenate([I,J],axis=0)) # 行连接
print(np.concatenate([I,J],axis=1)) # 列连接



# 数组切分
K = np.arange(36).reshape((6,6))
k1,k2 = np.hsplit(K,2) # 按列切分2等分 均分
print(k1)
k3,k4 = np.vsplit(K,2) # 按行切分2等分 均分
print(k3)

k5,k6,k7 = np.split(K,[2,3],axis=1)
#          - ary[:2]
#           - ary[2:3]
#           - ary[3:]
print(k7) # 按以上方式不等切分

# 对象的副本和视图
L = np.array([1,2,3,4])
M = L
N = L.copy()
L[2]=0
print(M)
print(L)
print(N) # 完整副本

# 矩阵结构化 为字段命名
O = np.array([("fist","2","哈哈"),
                ("irst","2","哈哈"),
                ("fis","2","哈哈")],dtype=[("wo","a6"),("ae","a6"),("yu","a6")])
O.dtype.names = ("who","are","you")
print(O["who"])


# 读取列表数据
P = np.genfromtxt("数据分析.txt", dtype=[('myint','i8'),('myfloat','f8'), ('mystring','U5')], delimiter=',',names=True)
print(P)
print(P.dtype)
print(P["商户编号"])