import os,sys
import pylab
import numpy as np
import matplotlib.pyplot as plt

#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

font =  {'family' : 'sans-serif',
         'color'  : 'black',
         'weight' : 'normal',
         'size'   : 16,
        }
y = np.loadtxt("AURO/1/qerr.mat", delimiter=' ')
x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(4)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,2],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,3],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=0, shadow=True, labelspacing=0,ncol=4,fontsize=18)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=4, mode="expand", borderaxespad=0)
#plt.grid(True)
plt.axis([0, 3000, 0, 0.15])

#plt.tight_layout()
y = np.loadtxt("AURO/100/qerr.mat", delimiter=' ')

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(0)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,2],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
plt.plot(x,y[:,3],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,4],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=0, shadow=True, labelspacing=0,ncol=4,fontsize=18)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=4, mode="expand", borderaxespad=0)
#plt.grid(True)
plt.axis([0, 3000, 0, 0.16])

#plt.tight_layout()

plt.show()
