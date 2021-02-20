import numpy as np
from matplotlib import pyplot as plt
x=[1,2,1,1]
l1=len(x)
h=[1,0,1]
l2=len(h)
N=l1+l2-1
y=np.zeros(N)
for i in range(l1,N+1):
	x.append(0)
for i in range(l2,N+1):
	h.append(0)
for n in range(N):
	for k in range(N):
		if(n>=k):
			y[n]=y[n]+x[n-k]*h[k]
print(y);
			
			

