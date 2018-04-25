#Shauna Byrne 24/04/2018
#Suggested final code including functions

import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plot

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')
dataset = pandas.read_csv('data/iris.csv')

print(data.shape)

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

def display(string, datas):
    meancol = numpy.mean(datas)
    mincol = numpy.min(datas)
    maxcol = numpy.max(datas)
    stdevcol = numpy.std(datas)
    mediancol = numpy.median(datas)

    print("Average of the %s column is : " % string, meancol)
    print("The minimum value in the %s column is :" % string, mincol)
    print("The maximum value in the %s column is :" % string, maxcol)
    print("The standard deviation of the %s column is: " % string, stdevcol)
    print("The median of the %s column is: " % string, mediancol)

    plot.hist(datas)
    plot.grid(True)
    plot.title(string)
    plot.show()

    plot.plot(datas)
    plot.grid(True)
    plot.title(string)
    plot.show()

display("Sepal Length", firstcol)
display("Sepal Width", secondcol)
display("Petal Length", thirdcol)
display("Petal Width", fourthcol)

plot.plot(firstcol, label='Sepal Length')
plot.plot(secondcol, label='Sepal Width')
plot.plot(thirdcol, label='Petal Length')
plot.plot(fourthcol, label='Petal Width')
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes in one

dataset.plot(kind='hist', subplots=True, layout=(2,2), sharex=False, sharey=False)
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes

dataset.plot(kind='line', subplots=True, layout=(2,2), sharex=False, sharey=False)
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes divided on one image

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes

dataset.plot(kind='area', subplots=False, layout=(2,2), sharex=True, sharey=True)
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes

scatter_matrix(dataset) 
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes

print(dataset.describe()) #all 4 attributes
