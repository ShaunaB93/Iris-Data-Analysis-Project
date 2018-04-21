#Shauna Byrne 19/04/2018
#Suggested code to run each of the 4 columns

import numpy
import pandas
import matplotlib.pyplot as plot
from scipy import stats

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')

print(data.shape)

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

meanfirstcol = numpy.mean(firstcol)
minfirstcol = numpy.min(firstcol)
maxfirstcol = numpy.max(firstcol)
stdevfirstcol = numpy.std(firstcol)
medianfirstcol = numpy.median(firstcol)
#modefirstcol = stats.mode(firstcol)
varifirstcol = numpy.var(firstcol)

print("Average of first column is: ", meanfirstcol)
print("The minimum value in the first column is :", minfirstcol)
print("The maximum value in the first column is :", maxfirstcol)
print("The standard deviation of the first column is: ", stdevfirstcol)
print("The median of the first column is: ", medianfirstcol)
#print("The mode of the first column is: ", modefirstcol)
#print("The variance of the first column is: ", varifirstcol)

plot.hist(firstcol)
plot.title('Sepal Length')
plot.show()

plot.hist(meanfirstcol)
plot.title('Mean Sepal Length')
plot.show()
