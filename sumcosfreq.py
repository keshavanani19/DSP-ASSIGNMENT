import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,250)
F1=200;p1=np.pi/3
F2=400;p2=np.pi/3
Fs=10000;
s1=20*np.cos(2*np.pi*F1/Fs*n+np.pi/2+p1)
plt.subplot(311);
plt.plot(n,s1);
s2=20*np.cos(2*np.pi*F2/Fs*n+np.pi/2+p2)
plt.subplot(312);
plt.plot(n,s2);
plt.subplot(313);
plt.plot(n,s1+s2);plt.show();
