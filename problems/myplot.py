#From week 10 class This is the way to do a plot using the package matplot
#however since the package remembers past actions or plots we can run it in a 
#Stateless Approach so it does not remember. 


import matplotlib.pyplot as plt
import numpy as np


x= np.linspace(1.0,10.0,1000)
y1= x*x
y2= x*x*x

fig, ax= plt.subplots() #in order to do so we use plt.subplots.

ax.plot (x,y1, label="x squared")
ax.plot (x, y2, label="x cubed")
ax.legend()
fig.show()

input()

