import os,sys
import pylab
import numpy as np
import matplotlib.pyplot as plt

font =  {'family' : 'sans-serif',
         'color'  : 'black',
         'weight' : 'normal',
         'size'   : 16,
        }

y0 = pylab.loadtxt("data/timing_nc_time/cfqp1.txt")
y1 = pylab.loadtxt("data/timing_nc_time/cfqp.txt")
y2 = pylab.loadtxt("data/timing_nc_time/nsqp.txt")
y3 = pylab.loadtxt("data/timing_nc_time/cflcp.txt")
y4 = pylab.loadtxt("data/timing_nc_time/nslcp.txt")
y0 = y0[y0[:,1]<2,:]
y1 = y1[y1[:,0]<2,:]
y2 = y2[y2[:,0]<2,:]
y4 = y4[y4[:,0]<2,:]
plt.figure(1)
sample = 1;
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.scatter(y0[::sample,2], y0[::sample,1],alpha=0.15, c='r',marker='v')
plt.scatter(y1[::sample,1], y1[::sample,0],alpha=0.15, c='g',marker='x')
plt.scatter(y2[::sample,1], y2[::sample,0],alpha=0.15, c='m',marker='o')
plt.scatter(y3[::sample,1], y3[::sample,0],alpha=0.15, c='k',marker='+')
plt.scatter(y4[::sample,1], y4[::sample,0],alpha=0.15, c='b',marker='D')

fit_fn = np.poly1d(np.polyfit(y0[:,2],y0[:,1],2))
x = np.linspace(1,40,40)
plt.plot(x,fit_fn(x),'r-v',label=r'$ID_{QP,\mu}^{one-stage}$')
fit_fn = np.poly1d(np.polyfit(y1[:,1],y1[:,0],2))
x = np.linspace(1,40,40)
plt.plot(x,fit_fn(x),'g-x',label=r'$ID_{QP,\mu}$')
fit_fn = np.poly1d(np.polyfit(y2[:,1],y2[:,0],2))
x = np.linspace(1,40,40)
plt.plot(x,fit_fn(x),'m-o',label=r'$ID_{QP,\infty}$')
fit_fn = np.poly1d(np.polyfit(y3[:,1],y3[:,0],2))
x = np.linspace(1,40,40)
plt.plot(x,fit_fn(x),'k-+',label=r'$ID_{LCP,\mu}$')
fit_fn = np.poly1d(np.polyfit(y4[:,1],y4[:,0],2))
x = np.linspace(1,40,40)
plt.plot(x,fit_fn(x),'b-D',label=r'$ID_{LCP,\infty}$')


ax = plt.subplot(111)
ax.set_xlim([0, 41])
ax.set_ylim([0, 2])
plt.legend(loc=8, shadow=True,columnspacing=0.25, labelspacing=0.25, ncol=5)

plt.title(r'Controller duration $vs.$ Contacts', fontdict=font)
plt.xlabel('Number of contacts', fontdict=font)
plt.ylabel('Execution time (ms)', fontdict=font)
plt.tight_layout()
plt.show()
