#Ainara Ruiz Castillo
# This program displays a plot of the functions f(x)=x ,g(x)=x2 and h(x)=x3 in the range [0,4]

import matplotlib.pyplot as plt
import numpy as np 

#After importing both libraries above I created variable x with range [0,4] evenly separated
x= np.linspace(0, 4, 10)

fig, ax= plt.subplots() #I created figure and an ax using Object oriented approach

f= x
g= x**2
h= x**3

ax.plot (f,f, label= "linear")
ax.plot (f,g,"r--", label=" squared")#After creating variables plot data in axes and added labels for each line.
ax.plot (f,h, label=" cubed")

ax.legend()#I added legend and title to plot
ax.set_title("My first plot")

fig.show()

input()#with this command I make the figure wait for input ( in this case close window) before stop showing

