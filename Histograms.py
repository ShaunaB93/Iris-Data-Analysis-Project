#Shauna Byrne 11/04/18
#Project Test Code from 2nd video 09/04/2018
#https://matplotlib.org/users/pyplot_tutorial.html - used to label the xaxis with the relevant descriptions
#Running code as Histograms.py in ipython leads to the histograms appearing one after the other once the previous diagram has been closed

import numpy

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:3]

import matplotlib.pyplot as plot
plot.hist(firstcol)
plot.xlabel('Sepal Length')
plot.show()

plot.hist(secondcol)
plot.xlabel('Sepal Width')
plot.show()

plot.hist(thirdcol)
plot.xlabel('Petal Length')
plot.show()

plot.hist(fourthcol)
plot.xlabel('Petal Width')
plot.show()
