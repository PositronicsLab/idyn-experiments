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
y = pylab.loadtxt("newdata/TRACKING-RIGID-TERRAIN.txt")

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(4)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
#plt.plot(x,y[:,1],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
#plt.plot(x,y[:,2],'--r',label=r'$ID(t_i)_{LCP,\mu}$',linewidth=3)
#plt.plot(x,y[:,3],':b' ,label=r'$ID(t_i)_{LCP,\infty}$',linewidth=3)
plt.plot(x,y[:,1],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,2],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
plt.plot(x,y[:,3],'--m' ,label=r'$ID(t_{i-2})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=0, shadow=True, labelspacing=0,ncol=4,fontsize=18)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=4, mode="expand", borderaxespad=0)
#plt.grid(True)
plt.axis([0, 5000, 0, 0.15])

plt.tight_layout()
y = pylab.loadtxt("newdata/TRACKING-RIGID-INF.txt")

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(0)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,1],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
plt.plot(x,y[:,2],'--r',label=r'$ID(t_i)_{LCP,\mu}$',linewidth=3)
plt.plot(x,y[:,3],':b' ,label=r'$ID(t_i)_{LCP,\infty}$',linewidth=3)
plt.plot(x,y[:,4],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,5],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
plt.plot(x,y[:,6],'--m' ,label=r'$ID(t_{i-2})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=0, shadow=True, labelspacing=0,ncol=4,fontsize=18)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
               ncol=4, mode="expand", borderaxespad=0)
#plt.grid(True)
plt.axis([0, 5000, 0, 0.25])

plt.tight_layout()
# /home/samzapo/Publications/ijrr-inverse-dynamics/images/error-rigid-inf.png

y = pylab.loadtxt("newdata/TRACKING-RIGID-0.1.txt")

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(1)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,1],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
plt.plot(x,y[:,2],'--r',label=r'$ID(t_i)_{LCP,\mu}$',linewidth=3)
plt.plot(x,y[:,3],':b' ,label=r'$ID(t_i)_{LCP,\infty}$',linewidth=3)
plt.plot(x,y[:,4],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,5],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
plt.plot(x,y[:,6],'--m' ,label=r'$ID(t_{i-2})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=9, shadow=True, labelspacing=0.5, borderpad=0.25)
#plt.grid(True)
plt.axis([0, 5000, 0, 0.15])

plt.tight_layout()


y = pylab.loadtxt("newdata/TRACKING-COMPLIANT-INF.txt")

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(2)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,1],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
plt.plot(x,y[:,2],'--r',label=r'$ID(t_i)_{LCP,\mu}$',linewidth=3)
#plt.plot(x,y[:,3],':b' ,label=r'$ID(t_i)_{LCP,\infty}$',linewidth=3)
plt.plot(x,y[:,3],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,4],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
plt.plot(x,y[:,5],'--m' ,label=r'$ID(t_{i-2})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=9, shadow=True, labelspacing=0.25,ncol=3)
#plt.grid(True)
plt.axis([0, 5000, 0, 0.20])

plt.tight_layout()


y = pylab.loadtxt("newdata/TRACKING-COMPLIANT-0.1.txt")

x = np.linspace(1,y[:,0].size,y[:,0].size)

plt.figure(3)
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.plot(x,y[:,0],'-k' ,label=r'$ID(t_i)_{QP,\mu}$',linewidth=3)
plt.plot(x,y[:,1],'-.g',label=r'$ID(t_i)_{QP,\infty}$',linewidth=3)
plt.plot(x,y[:,2],'--r',label=r'$ID(t_i)_{LCP,\mu}$',linewidth=3)
#plt.plot(x,y[:,3],':b' ,label=r'$ID(t_i)_{LCP,\infty}$',linewidth=3)
plt.plot(x,y[:,3],'-y' ,label=r'$PID$',linewidth=1)
plt.plot(x,y[:,4],'-.c' ,label=r'$ID(t_{i-1})$',linewidth=1)
plt.plot(x,y[:,5],'--m' ,label=r'$ID(t_{i-2})$',linewidth=1)
#plt.title('Positional trajectory tracking error for all joints (trotting quadruped)', fontdict=font)
plt.xlabel('Time (ms)', fontdict=font)
plt.ylabel(r'Average Position Error $E[|\theta-\theta_{des}|]$', fontdict=font)
#plt.legend(loc=9, shadow=True, labelspacing=0.5, borderpad=0.25)
#plt.grid(True)
plt.axis([0, 5000, 0, 0.15])

plt.tight_layout()
plt.show()

"""

y0 = pylab.loadtxt("data/timing-t0.txt")
y1 = pylab.loadtxt("data/timing-t1.txt")
y2 = pylab.loadtxt("data/timing-t2.txt")
y3 = pylab.loadtxt("data/timing-t3.txt")
x = pylab.loadtxt("data/timing-ncID.txt")
#colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses

plt.figure(1)
#plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.scatter(x, y0, c='r',marker='v',label=r'$ID(t_i)_{QP,\mu}$')
plt.scatter(x, y2, c='b',marker='D',label=r'$ID(t_i)_{QP,\infty}$')
plt.scatter(x, y1, c='g',marker='x',label=r'$ID(t_i)_{LCP,\mu}$')
plt.scatter(x, y3, c='k',marker='+',label=r'$ID(t_i)_{LCP,\infty}$')

ax = plt.subplot(111)
ax.set_xlim([0, 60])
ax.set_ylim([0, 150])
plt.legend(loc=2, shadow=True, labelspacing=0.5, fontsize=18)

plt.title(r'Controller duration $vs.$ Contacts', fontdict=font)
plt.xlabel('Number of contacts', fontdict=font)
plt.ylabel('Execution time (ms)', fontdict=font)
plt.tight_layout()
plt.show()

# (Sim Time,Forward Velocity)

"""
"""
plt.figure(0)
# max-event-time                            # inf
x = (435.9,457.4,616.3,2219.4,7958.4,9591.3)#,1569.3)
# avg x velocity over 10s
y = (5.50,5.52  ,5.62 ,5.65  ,5.78  ,5.74  )#,5.77)

plt.plot(x,y,'b-o')
plt.title('Average forward velocity over 10s, versus Simulation Time', fontdict=font)
plt.xlabel('Total simulation time (seconds)', fontdict=font)
plt.ylabel('Average forward velocity (cm/s)', fontdict=font)
plt.grid(True)




# (Sim Time,Stop Time)

plt.figure(1)
# max-event-time                            # inf
x = (5.57,5.65,23.31,179.66,228.73,284.26)#,17.26)
# avg x velocity over 10s
y = (270 ,273 ,244  ,234   ,233   ,234  )#,235)

plt.plot(x,y,'b-o')
plt.title('Time needed to stop wheel, versus Total Simulation Time', fontdict=font)
plt.xlabel('Total simulation time (seconds)', fontdict=font)
plt.ylabel('Time to stop wheel (milliseconds)', fontdict=font)
plt.grid(True)

# (time ,forward progress) w/ sub plot
fig_h = plt.figure(2)
plot_h = fig_h.add_subplot(111)
data = pylab.loadtxt("data_trot2/x_trot.mat")
# correct data offset (robot starts at -0.5)
data += 0.5
line_style = ('-o','-*','-s','-D','-+','-x','-|');
labels = ('0.0001s','0.001s','0.01s','0.1s','1s','10s','INFs');
for i in range(0, data.size/data[:,1].size):
  x = np.linspace(0,10,data[:,i].size)
  plot_h.plot(x[::550],data[::550,i],line_style[i],label=labels[i])

plt.title('Forward progress made by robot over time', fontdict=font)
plt.xlabel('Time (seconds)', fontdict=font)
plt.ylabel('Distance traveled (meters)', fontdict=font)
plt.legend(loc=4, shadow=True)

# Zoom on the first measurement
zoom_plot_h = zoomed_inset_axes(plot_h, zoom = 6.5, loc=2)
for i in range(0, data.size/data[:,1].size):
  x = np.linspace(0,10,data[:,i].size)
  zoom_plot_h.plot(x[9500::100],data[9500::100,i],line_style[i])

zoom_plot_h.set_xticks([])
zoom_plot_h.set_yticks([])
mark_inset(plot_h, zoom_plot_h, loc1=1, loc2=4, fc="none", ec="0.6")

# (subsequent solves, work done by impact), brake problem

plt.figure(3)
# avg x velocity over 10s
y = (-42.0505,-56.9107,-77.571,-77.571,-77.571,-77.571,-77.571,-84.151,-84.151,-84.151,-84.151,-84.151,-89.811)
x = range(1,14)
print x
print y

plt.plot(x,y,'r-o')
plt.title('Energy dissipated over one "progressive" solve', fontdict=font)
plt.xlabel('Anytime Algorithm Iterations', fontdict=font)
plt.ylabel('Work performed by solution', fontdict=font)
plt.xticks(range(1,14))
#plt.grid(True)
"""

plt.show()
