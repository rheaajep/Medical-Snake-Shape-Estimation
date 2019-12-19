# 2 link robot 
#for basis function 'x^2'
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
x2=sym.Symbol('x2')
x1=sym.Symbol('x1')
y1=sym.Symbol('y1')
y2=sym.Symbol('y2')
a1=sym.Symbol('a1')
a2=sym.Symbol('a2')
deltax2=sym.Symbol('deltax2')
deltay2=sym.Symbol('deltay2')
theta1=sym.Symbol('theta1')
theta2=sym.Symbol('theta2')
theta1new=sym.Symbol('theta1new')
theta2new=sym.Symbol('theta2new')
l1=1
l2=1
#finding the x positions by solving y=x^2
x1=0.62
x2=1.24
y1=x1**2
y2=x2**2

#now we modify the shape of the end effector
deltax2=0
deltax2plot=[]
x2newplot=[]
a1_plot=[]
a2_plot=[]

for i in range(10):
    deltay2=i*0.01
    x2new=x2-deltax2
    y2new=y2-deltay2
    theta2new=math.acos((x2new**2+y2new**2-l1**2-l2**2)/2*l1*l2)
    theta1new=math.atan(y2new/x2new)-math.atan((l2*math.sin(theta2new))/l1+l2*math.cos(theta2new))
    x1new=l1*math.cos(theta1new)
    y1new=l1*math.sin(theta1new)
    solution=sym.solve((a1*x2new+(a2*(x2new**2))-y2new,a1*x1new+(a2*(x1new**2))-y1new),(a1,a2))
    a1_sol=solution[a1]
    a2_sol=solution[a2]
    deltax2plot.append(deltay2)
    a1_plot.append(a1_sol)
    a2_plot.append(a2_sol)

fig=plt.figure()
plt.plot(deltax2plot,a1_plot)
plt.savefig('C:/Users/rheap/Documents/CMU/BioRobotics lab/results/2_link_x2_a1plot')
plt.show()

fig2=plt.figure()
plt.plot(deltax2plot,a2_plot)
plt.savefig('C:/Users/rheap/Documents/CMU/BioRobotics lab/results/2_link_x2_a2plot')
plt.show()
    