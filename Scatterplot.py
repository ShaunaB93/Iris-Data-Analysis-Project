#Shauna Byrne 15/04/2018

import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plot

file = "data/iris1.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(file, names=names)

scatter_matrix(dataset)
plot.show()
