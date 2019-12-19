# 3 link robot 
#for basis function 'x2'
#changed gamma is 45 degrees 
from sympy.interactive import printing 
printing.init_printing(use_latex=True)
import numpy as np 
import sympy as sym
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import math


#ax=plt.axes(projection='3d')

y1new=sym.Symbol('y1new')
x1new=sym.Symbol('x1new')
y2new=sym.Symbol('y2new')
x2new=sym.Symbol('x2new')
x3new=sym.Symbol('x3new')
y3new=sym.Symbol('y3new')
x2=sym.Symbol('x2')
x1=sym.Symbol('x1')
x3=sym.Symbol('x3')
y1=sym.Symbol('y1')
y2=sym.Symbol('y2')
y3=sym.Symbol('y3')
a1=sym.Symbol('a1')
a2=sym.Symbol('a2')
a3=sym.Symbol('a3')
deltax3=sym.Symbol('deltax3')
deltay3=sym.Symbol('deltay3')
theta1=sym.Symbol('theta1')
theta2=sym.Symbol('theta2')
theta3=sym.Symbol('theta3')
theta1new=sym.Symbol('theta1new')
theta2new=sym.Symbol('theta2new')
theta3new=sym.Symbol('theta3new')
gamma=sym.Symbol('gamma')

#defining values
l1=1
l2=1
l3=1
gamma=0.901

#finding the x positions by solving y=x^2
x1=0.62
x2=x1*2
x3=x2*2
y1=x1**2
y2=x2**2
y3=x3**2

#now we modify the shape of the 2nd link
deltax3=0
deltax3plot=[]
x3newplot=[]
a1_plot=[]
a2_plot=[]
a3_plot=[]

for i in range(10):
    deltay3=i*0.01
    x3new=x3-deltax3
    y3new=y3-deltay3
    x2new=x3new-l3*math.cos(gamma)
    y2new=y3new-l3*math.sin(gamma)
    print(x2new)
    print(y2new)
    print((x2new**2+y2new**2-l1**2-l2**2)/2*l1*l2)
    theta2new=math.acos((x2new**2+y2new**2-l1**2-l2**2)/2*l1*l2)
    theta1new=math.atan(y2new/x2new)-math.atan((l2*math.sin(theta2new))/l1+l2*math.cos(theta2new))
    theta3new=gamma-(theta1new+theta2new)
    x1new=l1*math.cos(theta1new)
    y1new=l1*math.sin(theta1new)
    solution=sym.solve((a1*x3new+(a2*(x3new**2))+(a3*(x3new**3))-y3new,a1*x2new+(a2*(x2new**2))+(a3*(x2new**3))-y2new,a1*x1new+(a2*(x1new**2))+(a3*(x1new**3))-y1new),(a1,a2,a3))
    a1_sol=solution[a1]
    a2_sol=solution[a2]
    a3_sol=solution[a3]
    deltax3plot.append(deltay3)
    a1_plot.append(a1_sol)
    a2_plot.append(a2_sol)
    a3_plot.append(a3_sol)

#a1 plot
fig=plt.figure()
plt.plot(deltax3plot,a1_plot)
plt.savefig('C:/Users/rheap/Documents/CMU/BioRobotics lab/results/3_link_x2_a1plot')
plt.show()

#a2 plot
fig2=plt.figure()
plt.plot(deltax3plot,a2_plot)
plt.savefig('C:/Users/rheap/Documents/CMU/BioRobotics lab/results/3_link_x2_a2plot')
plt.show()

#a3 plot
fig3=plt.figure()
plt.plot(deltax3plot,a3_plot)
plt.savefig('C:/Users/rheap/Documents/CMU/BioRobotics lab/results/3_link_x2_a3plot')
plt.show()


    