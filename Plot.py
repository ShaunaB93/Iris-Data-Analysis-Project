#Shauna Byrne
#Iris Data Set Analysis 17/04/18
#https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
#https://matplotlib.org/users/pyplot_tutorial.html

import numpy
data = numpy.genfromtxt('data/iris.csv', delimiter=',')
import matplotlib.pyplot as plot

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:3]

plot.plot(firstcol)
plot.grid(True)
plot.title('Sepal Length')
plot.show()

plot.plot(secondcol)
plot.grid(True)
plot.title('Sepal Width')
plot.show()

plot.plot(thirdcol)
plot.grid(True)
plot.title('Petal Length')
plot.show()

plot.plot(fourthcol)
plot.grid(True)
plot.title('Petal Width')
plot.show()
