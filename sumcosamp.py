import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,250)
F1=250;p1=np.pi/3
F2=250;p2=np.pi/3
Fs=10000;
s1=0.5*np.cos(2*np.pi*F1/Fs*n+np.pi/2+p1)
plt.subplot(311);
plt.stem(n,s1);
s2=0.8*np.cos(2*np.pi*F2/Fs*n+np.pi/2+p2)
plt.subplot(312);
plt.stem(n,s2);
plt.subplot(313);
plt.stem(n,s1+s2);plt.show();
