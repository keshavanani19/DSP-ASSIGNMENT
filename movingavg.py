import numpy as np
from matplotlib import pyplot as plt
y=10*np.random.rand(100)
z=np.zeros(len(y))
M=int(input('enter order'))
for n in range (0,len(y)):
   s=0
for k in range(0,M):
   if n-k>=0:
      s=s+y[n-k]
      z[n]=s/M
print(y)
print(z)
plt.subplot(2,1,1)
plt.plot(y)
plt.subplot(2,1,2)
plt.plot(z)
plt.show()
