import numpy as np
from matplotlib import pyplot as plt
M= int(input("Enter the value of M "))
x=[1,2,3,4,5]
y=[]
for i in range(0,5):
	sum1=0
	for j in range(0,M):
		if(i-j>=0):
			sum1=sum1+x[i-j]
	y.append(sum1/M)
for k in range(0,5):
	print(y[k])
plt.subplot(2,1,1)
plt.stem(x)
plt.subplot(2,1,2)
plt.stem(y)
plt.show()	 
