#Shauna Byrne 21/04/2018
#Iris Data Set Analysis
#Complete draft code summarising data set - example of column one which would need to be repeated until graphs containing all 4 attributes for each of the columns of data
#As code appears quite bulky in this format to include all 4 column analysis - ideal outcome would be to create a function which would call the calculations for all 4 columns in order to cut the amount of code & for it to be easier to follow

import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plot
from scipy import stats

data = numpy.genfromtxt('data/iris1.csv', delimiter=',')
dataset = pandas.read_csv('data/iris.csv')

print(data.shape)

SepalLength = data[:,0]
SepalWidth = data[:,1]
PetalLength = data[:,2]
PetalWidth = data[:,3]
Class = data[:,4]

#SepalLength1 = dataset[:,0]
#SepalWidth1 = dataset[:,1]
#PetalLength1 = dataset[:,2]
#PetalWidth1 = dataset[:,3]
#Class1 = dataset[:,4]

meanseplencol = numpy.mean(SepalLength)
minseplencol = numpy.min(SepalLength)
maxseplencol = numpy.max(SepalLength)
stdevseplencol = numpy.std(SepalLength)
medianseplencol = numpy.median(SepalLength)
#modeseplencol = stats.mode(SepalLength)
#variseplencol = numpy.var(SepalLength)

print("Average of first column is: ", meanseplencol)
print("The minimum value in the first column is :", minseplencol)
print("The maximum value in the first column is :", maxseplencol)
print("The standard deviation of the first column is: ", stdevseplencol)
print("The median of the first column is: ", medianseplencol)
#print("The mode of the first column is: ", modeseplencol)
#print("The variance of the first column is: ", variseplencol)

plot.hist(SepalLength)
plot.grid(True)
plot.title('Sepal Length')
plot.show()

plot.hist(meanseplencol)
plot.grid(True)
plot.title('Mean Sepal Length')
plot.show()

plot.plot(SepalLength)
plot.grid(True)
plot.title('Sepal Length')
plot.show()

plot.plot(SepalLength, label='Sepal Length')
plot.plot(SepalWidth, label='Sepal Width')
plot.plot(PetalLength, label='Petal Length')
plot.plot(PetalWidth, label='Petal Width')
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes in one

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plot.grid(True)
plot.legend()
plot.show() #all 4 attributes in one

scatter_matrix(dataset) #all 4 attributes in one
plot.grid(True)
plot.legend()
plot.show()

