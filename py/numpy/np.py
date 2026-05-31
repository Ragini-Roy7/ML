import numpy as np
import matplotlib.pyplot as plt

nums= [12,45,67,323,454]
arr= np.array(nums)
print(arr)
print(type(arr))

matrix= [[1,2,3,4,5,6], [4,5,6,7,8,9], [6,7,8,9,6,7]]
mat=np.array(matrix)
print(mat)
print(mat.shape)

#arange()
print (np.arange(0, 19, 1))

#zeroes
print(np.zeros(6))

#integer zeros
c=np.zeros((4,3),dtype=int)
print(c)

#linspace()
# numpy.linspace(start,stop,num)
d=np.linspace(0,11,7)
print(d)

#decimal range
dec= np.linspace(1,5,12)
print(dec)

x= np.linspace(-5,5,10)
print(x)

#y values
y=x**3
plt.plot(x,y)
#creating labels
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("graph of y =x")
# plt.show()

# num= np.linspace(10,5,100)
# print(num)

#identity matrix using methods
print(np.eye(4))

#random array from 0 to 1
random_arr=np.random.rand(5,5)
print(random_arr)
#using gaussian un-uniformed distribution 
print (np.random.randn(3))