#Shauna Byrne 14/04/2018
#Additional Project Code work to test .describe function.
#Dataframes usually used to summarize datasets/summary of each attribute such as count, mean, the min and max values as well as some percentiles in the case of numeric data - suggested as alternate shorted method of outlining the Iris Datasets information in a neater fortmat
#From research code returned errors so an alternate method to produce required results was researched - this can be found in Describe2 commit.
import pandas
import os

#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

file = "data/iris.csv"
data = pandas.read_csv(file, encoding ='utf-8')

print(type(data))
data ['sepal length'].describe()
