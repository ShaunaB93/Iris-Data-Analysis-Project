#Shauna Byrne 14/04/2018
#Additional Project Code work to test .describe function as outlined in link on comment 4
#Testing of Data frames which have been mentioned on numerous web links for similar projects.
#Dataframes usually used to summarize datasets/summary of each attribute such as count, mean, the min and max values as well as some percentiles in the case of numeric data - suggested as alternate shorted method of outlining the Iris Datasets information in a neater fortmat
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html
#https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import pandas
import os

#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

file = "data/iris.csv"
data = pandas.read_csv(file, encoding ='utf-8')

print(type(data))
data ['sepal length'].describe()
