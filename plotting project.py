import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

# now plot
plt.plot(X,C)
plt.plot(X,S)

plt.show()

#create a fig with size 8*6 inches 80 dots per inch
plt.figure(figsize=(8,6), dpi=80)

#subplot creation
plt.subplot(1,1,1)

plt.plot(X,C, color="blue", linewidth =1.0, linestyle = "-")
plt.plot(X,C, color="green", linewidth =1.0, linestyle = "-")

plt.plot(X,C, color="blue", linewidth =2.5, linestyle = "-")
plt.plot(X,S, color="red", linewidth =2.5, linestyle = "-")
#set x limits
plt.xlim(-4.0, 4.0)

# set x ticks
plt.xticks(np.linspace(-4,4,9, endpoint=True))
plt.ylim(-1,1)
plt.yticks(np.linspace(-1,1,5, endpoint=True))
#save fig
#plt.savefig("exercise_2.png", dpi = 72)

plt.plot(X,C, color="blue", linewidth =2.5, linestyle = "-")
plt.plot(X,S, color="red", linewidth =2.5, linestyle = "-")
plt.xlim(X.min() * 1.1, X.max()*1.1)
plt.ylim(C.min() * 1.1, C.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1,0,+1])

#seting tick label on the plot
#xtick after a variable is the label
#tick  = no of points and labels on a plot,
plt.plot(X,C, color="blue", linewidth =2.5, linestyle = "-")
plt.plot(X,S, color="red", linewidth =2.5, linestyle = "-")
plt.xlim(X.min() * 1.1, X.max()*1.1)
plt.ylim(C.min() * 1.1, C.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$',r'$-\pi/2$'])

#moving spines
plt.plot(X,C, color="blue", linewidth =2.5, linestyle = "-",label = "cosine")
plt.plot(X,S, color="red", linewidth =2.5, linestyle = "-", label = "sine")
plt.xlim(X.min() * 1.1, X.max()*1.1)
plt.ylim(C.min() * 1.1, C.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$',r'$-\pi/2$'])
#axis component
ax = plt.gca()#get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#legend
plt.legend(loc='upper left')


#annotate some points i.e tag a position
t = 2 * np.pi / 3
plt.plot([t,t], [0,np.cos(t)], color = 'blue', linewidth = 2.5, linestyle = "--" )
plt.scatter([t, ], [np.cos(t),], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi} {3} = -\frac{1}{2})$', xy=(t,np.cos(t)), xycoords='data', xytext = (-90,-50), \
             textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))

#decil in the details
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor= 'None', alpha = 0.65))

#regular plots
n = 256
Y = np.sin (2 * X)

#fill some parts
plt.axes([0.025,0.025,0.95,0.95])
plt.plot(X,Y +1, color ='blue', alpha = 1.00)
plt.plot(X,Y - 1, color ='blue', alpha = 1.00)
plt.fill_between (X, -1,Y-1, alpha = 0.25)
plt.fill_between (X, -1,Y-1, (Y-1) < -1,color = 'red' , alpha = 0.25)

plt.xlim(-np.pi, np.pi)
plt.xticks()
#scatter plots
np.random.seed(12)
n =  1024
A = np.random.normal(0,1,n)
B = np.random.normal(0,1,n)

T = np.arctan2(B,A)
plt.axes([0.025,0.025,0.95,0.95])
plt.scatter (A,B, s=75,c=T, alpha=.5)

#bar plot
np.random.seed(12)
n=12
D = np.arange(n)
YI = (1-D/float(n)* np.random.uniform(.5,1,n))
Y2 = (1-D/float(n)* np.random.uniform(.5,1,n))
plt.axes([0.025,0.025,0.95,0.95])
plt.bar(D, +YI, facecolor='#9999ff', edgecolor= 'white')
plt.bar(D, -Y2, facecolor='#ff9999', edgecolor= 'white')

for x,y in zip(D, YI) :
    plt.text(x + 0.2, y +0.05, '%.2f' %y, ha='center', va ='bottom')

plt.ylim(-1.25, 1.25)
plt.yticks(())

#piechart
np.random.seed(12)
Z = np.random.uniform(0,1,20)
plt.hist(Z)

#quiver plot
 n = 8
 X,Y = np.mgrid [0:n, 0:n]
plt.quiver(X,Y)
