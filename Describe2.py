#Shauna Byrne 14/04/2018
#Additional Project Code work to test .describe function as outlined in link on comment 4
#Testing of Data frames which have been mentioned on numerous web links for similar projects.
#Dataframes usually used to summarize datasets/summary of each attribute such as count, mean, the min and max values as well as some percentiles in the case of numeric data - suggested as alternate shorted method of outlining the Iris Datasets information in a neater fortmat
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
#https://www.dataquest.io/blog/pandas-cheat-sheet/

#this code ran correctly when running in ipython using the "run Describe2.py" command & gives output for the count, mean, standard deviation, minimum, 25%, 50%, 75% & maximum values calculatied for each attribute colmn.
import pandas

file = "data/iris1.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(file, names=names)

#reviews how many instances (rows) and how many attributes (columns) the data contains with the shape property.
print(dataset.shape)

#should summarise each attribute - count, mean, the min and max values as well as some percentiles
#Code currently appears to be giving different attributes due to file information in iris.csv file which contains attribute headings in the first row
#using iris file with headings output is count,unique,top & freq for this function.
#using iris1 file without headings gives relevant information.
print(dataset.describe())
