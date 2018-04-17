#Shauna Byrne 12/04/18
#Extracted from previous Histograms.py file but altered to show the mean of each column of data on a Histogram.
#https://matplotlib.org/users/pyplot_tutorial.html - Used to add titles to the Histogram rather than the X axis labels used in Histograms.py
#Running code as Meanhist.py in ipython leads to the histograms appearing one after the other once the previous diagram has been closed

import numpy

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')

meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanfourthcol = numpy.mean(data[:,3])

import matplotlib.pyplot as plot
plot.hist(meanfirstcol)
plot.title('Mean Sepal Length')
plot.show()

plot.hist(meansecondcol)
plot.title('Mean Sepal Width')
plot.show()

plot.hist(meanthirdcol)
plot.title('Mean Petal Length')
plot.show()

plot.hist(meanfourthcol)
plot.title('Mean Petal Width')
plot.show()
