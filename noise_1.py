import scipy.io.wavfile
import numpy as np
from matplotlib import pyplot as plt
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
fs,x=scipy.io.wavfile.read('mom-1.wav')
print(x.shape)
print(fs)
X=[]
j=(-1)**0.5
for i in w:
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*j*i*n)
	X.append(s)
plt.subplot(2,1,1);
plt.plot(w,np.abs(X))
plt.subplot(2,1,2);
plt.plot(w,np.angle(X))
plt.show();
