#Shauna Byrne 15/04/18
#To be added to main calculations of mean,min & max

import numpy as numpy
from scipy import stats

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')
#numpy.set_printoptions(precision = 3)

firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]

stdevfirstcol = numpy.std(firstcol)
stdevsecondcol = numpy.std(secondcol)
stdevthirdcol = numpy.std(thirdcol)
stdevfourthcol = numpy.std(fourthcol)

print("The standard deviation of the first column is: ", stdevfirstcol)
print("The standard deviation of the second column is: ", stdevsecondcol)
print("The standard deviation of the third column is: ", stdevthirdcol)
print("The standard deviation of the fourth column is: ", stdevfourthcol)

medianfirstcol = numpy.median(firstcol)
mediansecondcol = numpy.median(secondcol)
medianthirdcol = numpy.median(thirdcol)
medianfourthcol = numpy.median(fourthcol)

print("The median of the first column is: ", medianfirstcol)
print("The median of the second column is: ", mediansecondcol)
print("The median of the third column is: ", medianthirdcol)
print("The median of the fourth column is: ", medianfourthcol)

modefirstcol = stats.mode(firstcol)
modesecondcol = stats.mode(secondcol)
modethirdcol = stats.mode(thirdcol)
modefourthcol = stats.mode(fourthcol)

print("The mode of the first column is: ", modefirstcol)
print("The mode of the second column is: ", modesecondcol)
print("The mode of the third column is: ", modethirdcol)
print("The mode of the fourth column is: ", modefourthcol)

varifirstcol = numpy.var(firstcol)
varisecondcol = numpy.var(secondcol)
varithirdcol = numpy.var(thirdcol)
varifourthcol = numpy.var(fourthcol)

print("The variance of the first column is: ", varifirstcol)
print("The variance of the second column is: ", varisecondcol)
print("The variance of the third column is: ", varithirdcol)
print("The variance of the fourth column is: ", varifourthcol)
