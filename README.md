# Draft Programming & Scripting Data Analysis Project of Iris Flower Data Set

## Abstract - Background Information of the Iris data set - 

In 1936 a study was first published by Ronald Fisher in the paper *"The use of multiple measurements in taxonomic problems".*

<img src="https://upload.wikimedia.org/wikipedia/commons/4/46/R._A._Fischer.jpg" width="200" height="200">

*Ronald Fisher* 

This data set is now widely known & analysed in studies in various areas such as pattern recognition literature, machine learning, statistics, data mining & various other fields [4]. The data set is preferred for testing projects in these fields as the attributes are numeric and in the same units, which means loading and handling the data are required but no special scaling is required, it is a multi-classification problem, which allows for testing of learning algorithms & specialised handling and its size, only containing 4 attributes & 150 rows.

The data set itself describes particular biological characteristics of various sample Iris flowers. The study contains data relating to three classes of iris flowers – Iris Setosa, Irisa Versicolour & Iris Virginica, with fifty instances of each class analysed in the study. 

<img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg" width="200" height="200">

*Iris Setosa*

<img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg" width="200" height="200">

*Iris Versicolour*

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg" width="200" height="200">

*Iris Virginica*

The analysis of each instance calculates the – Sepal Length, Sepal Width, Petal Length & Petal Width. Generally the data set is analysed to test algorithms developed to classify the type of iris flower based on the measurements provided. Previous studies completed on the data set have determined that each class is linearly separable from the other two [6]. 

The dataset can be viewed [here](https://archive.ics.uci.edu/ml/datasets/iris)

### Introduction – 
As per the project statement the following was the outline provided for the project – 

*“The following project concerns the well-known Fisher’s Iris data set [1]. The project entails you researching the data set, and then writing documentation and code in the
Python programming language based on that research. An online search for information on the data set will convince you that many people have investigated and written about it previously, and many of those are not experienced programmers. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed. You might do that for this project as follows:
1. Research background information about the data set and write a summary about it.
2. Keep a list of references you used in completing the project.
3. Download the data set and write some Python code to investigate it.
4. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.
5. Write a summary of your investigations.
6. Include supporting tables and graphics as you deem necessary.”*

Following the issue of the project objective I decided to put a plan together on how to approach the project. I started this by researching similar projects completed using the iris flower dataset, as it is widely used. Following to this research I was able to determine the analysis calculations and graphs I believed would be useful in this project in order to analyse the dataset provided, which was followed by determining how the project should fit together. Throughout the research, I came across numerous calculations & graphs which could be use to analyse the dataset. The various suggestions of calculations & graphs can be seen in the alternate commits of code represented in the different files of this repository with the [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) commit representing the code being submitted for this assignment.

As a starting point, I began to work from the lecture material posted on how to hard code calculations i.e. the mean & put together histograms in python. After watching & gaining an understanding of the code used in the lecture videos I started out the project using similar code to do some calculations which can be seen in the alternate commit files in this repository mentioned previously. I quickly determined there was a lot of repetition of code & that the code would become quite large using this method even for a relatively small data set. While researching methods of coding such analysis I came across the use of the *.describe* function, which will be discussed in detail later, as an alternate method for some parts of the code I wanted to use for the analysis. Following on from this determination that the code contained a lot of repetition of specific lines of code & due to its size, I believed creating a function may be the best route to tackle both issues at once. This led to the method that I used to decide on my final code, seen in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), as I wanted it to include the calculations I deemed necessary while keeping the code as clean and easy to read as possible for anyone reviewing this later, which I believe was made possible using the function as to include the information I wished to hard-coding this would have taken roughly 500 lines while using the function allowed me to reduce this to 80 lines. Each individual stage also took some error resolution steps as some of the researched code required some work in order for it to function with other lines of code. 

From carrying out research for the project measuring the central tendency of a dataset can be the most descriptive method of determining a population’s characteristics as they describe the average member of the population of interest. In order to determine the central tendency of a population the mean, median and mode are generally calculated. For this project I have decided to calculate only the mean & median of the dataset. I have made this decision as the mean of a dataset is the most commonly measured feature of central tendency & includes every value in the data set as part of the calculation while the median is useful for determining skewed distribution of data by comparison to the output of the mean value. [2][3][4]

### Method of Code –
**- A)	Libraries to be imported:**
The code produced in the [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) file commit begins by having python installed via Anaconda & importing the following libraries for the analysis mentioned later in the commit to work. The commands can also be ran in *ipython* but appears as a script in the [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) commit - 
 
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/5gybwp4k3/Libraries.jpg" alt="Libraries"/></a><br/><br/>
 
**- B) Shape of the data set:**

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/vci2fsqxf/Shape.jpg" alt="Shape"/></a><br/><br/> [5]

The analysis of the data represented of line 12 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) provides an overview of the number of instances or rows & attributes or columns the data set contains. This code has been included for informative purposes to give the analyst an idea of the size of the data set being examined [5].

**- C)	Calculation function:** 

<img src="https://s19.postimg.cc/3p5d1rimb/Calculation_Function.jpg" alt="Calculation_Function"/></a><br/><br/>
 
The above commands can be ran to calculate the mean, minimum, maximum & standard deviation of each of the attribute columns in the iris flower dataset. It also produces histograms & line graphs for each of the attributes grouped together for each of the calculations. The calculations & graphs have been grouped in a function to firstly cut the code to avoid repetition in order to calculate the values for each column & to ensure the information for each of the values appear one after the other for the ease of viewing of the results. 
   * 1)	The mean of a dataset is known as a descriptive statistic which can be used as a measure of central tendency as mentioned previously. In order to calculate the mean, all values within the specified dataset are added & the sum is divided by the number of values. In the case of the above mentioned piece of code outlined on line 20 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), the calculation of the mean has been completed for each of the attribute columns within the iris flower dataset. However, it is widely known that there is a disadvantage to calculating the mean during data analysis as it is susceptible to outlier values within the dataset which can skew the results. The above code example was successful in calculating the mean of each of the columns mentioned when compared to alternate code found during the research for the project when used to confirm the values[2][3][4].


   * 2)	Calculating the minimum & maximum are also useful for providing an understanding of the dataset being analysed. While the min indicates the lowest observation, the max represents the highest observation. By calculating both values for a given data set it assists in understanding the span of the data by analysing it rather than having to read through the whole file in order to determine the information, while it can also be an indication of an error. Similar to the calculations mentioned previously, the above mentioned piece of code outlined on line 27 & 28 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), the calculation of the min & max has been completed for each of the columns within the iris flower dataset. The output for each column of dataset gives the person observing or testing the data the span of the information/values provided in each column [6].


   * 3)	The standard deviation is generally calculated as a measure of the variability or the spread of scores within the data being examined. This value provides a useful view as to how variable the data set is & is another commonly used statistic for analysing data [7][19]. The calculation of the standard deviation is usually carried out alongside the mean when summarising data in cases of continuous data. This is useful in the analysis of the iris flower data set as it contains nominal variables. However, similar to the calculation of the mean it can be affected by outliers in the dataset which can skew the results [9]. Similar to the calculations mentioned previously, the above mentioned piece of code outlined on line 29 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), the calculation of the standard deviation has been completed for each of the columns within the iris flower dataset. 

   * 4)	Calculating the median of a data set is also known as a descriptive statistic, similar to calculating the mean. The median is widely known as the value that is the middle value of a set of specific values from a dataset, or the entire dataset. This would indicate that 50% of the values within the dataset are below the median while the remaining 50% are above the median. As the mean can distort the produced data or image relating to the data set if there are any outliers, the median can assist by locating this middle value as an additional analysis & comparative tool. Descriptive statistics are generally used to describe the sample being analysed. While they give the analyst a general outline of the data being analysed, they are also statistical tests & can be used to indicate errors associated with results and any graphical outputs produced [19]. Similar to the calculation of the mean mentioned previously, the above mentioned piece of code outlined on line 30 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), the calculation of the median has been completed for each of the columns within the iris flower dataset. 

   * 5)	The next grouping of code in the function produces individual histograms for each of the attribute columns. Histograms are useful when analysing data as they provide a visual representation of the underlying frequency distribution or shape of, in this case, a continuous data set. The code used to produce this output in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) can be viewed on lines 32 through 35 of the script. By providing this output in order to analyse the data set it allows for the inspection of the data in its distribution & also if there are any outlier values which represent a skewness within the data set [8]. The outputs of this visualisation of the data contained in the individual columns of the iris data set were as follows –

 <img src="https://s19.postimg.cc/7ya33vw5f/Sepal_Length_Individual_Histogram.png" alt="Sepal_Length_Individual_Histogram"/></a><br/><br/>
 <a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/ua7vx9njn/Sepal_Width_Individual_Histogram.png" alt="Sepal_Width_Individual_Histogram"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/lryft0orn/Petal_Length_Individual_Histogram.png" alt="Petal_Length_Individual_Histogram"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/njrenxnk3/Petal_Width_Individual_Histogram.png" alt="Petal_Width_Individual_Histogram"/></a><br/><br/>
 
   * 6)	The value of line plots for data analysis is very similar to that produced from bar charts as they both compare values. Each data point has an X & Y value which are then connected by lines. Line charts are generally used when analysing data to emphasize overall trends or patterns within the data set provided [10]. This visual analysis has been coded in three different formats within lines 37 to 40, lines 47 to 53 & line 60 to 63 in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py). The first visualisation represents the singular line plots to represent the data in the individual columns – sepal length, sepal width, petal length & petal width [11]. The second grouping of code shows the data from all four columns on one line plot to allow for comparisons to be made while the data is represented alongside the alternate three columns. While the last group of code produces four individual line plots within one figure to allow for an alternate view/visualisation of the data. Each instance allows for a different representation & comparison opportunity for the four individual columns of data as well as being compared against one another. The outputs of this visualisation of the data contained in the individual columns of the iris data set were as follows – 
 
 <a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/90k9mfueb/Sepal_Length_Individual_Plot.png" alt="Sepal_Length_Individual_Plot"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/w20us6mc3/Sepal_Width_Individual_Plot.png" alt="Sepal_Width_Individual_Plot"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/7lioxslmb/Petal_Length_Individual_Plot.png" alt="Petal_Length_Individual_Plot"/></a><br/><br/>
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/lf71mutn7/Petal_Width_Individual_Plot.png" alt="Petal_Width_Individual_Plot"/></a><br/><br/>
 
**- D) Line (4 attributes 1 graph):**

 <a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/rg4qjxvoz/Plot_Graph_4_lines_1_image.jpg" alt="Plot_Graph_4_lines_1_image"/></a><br/><br/> [12]

The above section of code, seen on lines 47 through 53, represents the data from all four attribute columns on one line plot. Each line represents each of the attribute columns, as the legend [13] included informs which column is indicated by the different colour line plots represented. This was prodcued as an alternate view for comparison of the information visualised, such as the trend of the data contained in each column within the data set, via the line plots. 

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/s5niwb3yb/Plot_Graph_1_image.png" alt="Plot_Graph_1_image"/></a><br/><br/>
 
**- D) Histograms for each attribute individually in one image:**

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/r3dcdpver/Histogram_all_in_one_image_individually.jpg" alt="Histogram_all_in_one_image_individually"/></a><br/><br/> [14]

The section of code outlined in the image above, & on lines 55 through 58 in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), produces the four individual histograms within one figure, each individual histogram is labelled to allow for the identification of the column of data is represented through the titles included. As mentioned previously the histograms offer an alternate visual representation of the shape of the data from the data set analysed in this project. By producing the histograms alongside the data from the alternate attribute columns it allows for a closer comparison to be made rather than the viewer having to remember the individual histograms produced earlier in the script.

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/fr0qvwzkj/Four_Histograms.png" alt="Four_Histograms"/></a><br/><br/>
 
**- F) Line plot for each attribute individually in one image:**

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/aflub9axv/Plot_all_in_one_image_individually.jpg" alt="Plot_all_in_one_image_individually"/></a><br/><br/> [14]

This section of code, represented on lines 60 through 63 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), produces four individual line plots within one figure, each individual line plot is labelled to allow for the identification of the column of data is represented through the titles included. This was prodcued as an alternate view for comparison of the information visualised, to the individually produced line plots & the single line plot containing all four columns. Each of the differing line plots produced clearly show the trend of the data contained in each column within the data set. 

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/om1l6fw2r/Four_Plot_Graphs.png" alt="Four_Plot_Graphs"/></a><br/><br/>
 
**- G) Box plot for each attribute individually in one image:**

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/qduk1bcur/Box_all_in_one_image_individually.jpg" alt="Box_all_in_one_image_individually"/></a><br/><br/> [14]

The above lines of code, represented on lines 65 through 68 of [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), produce four individual box plots each representing the attribute column listed in the title such as sepal length, sepal width, petal length & petal width of the iris flowers. Similar to the other analysis completed throughout this project this box plots are known as descriptive statistical representations of data. The individual box plots are a graphical method of displaying the variation, shape & median of each of the columns mentioned within the iris data set. It is used in addition to the histograms and line plots produced in this case in order to provide additional detail to the analysis. The box plot outputs can provide information as to whether the data being analysed is symmetric, with the median in the middle of the box, or skewed, with the median cuts the box into unequal sections. The median is shown by the line that cuts through the box plot. If the data is skewed & the median populates towards one side of the box, left or right, the dataset is said to be skewed right or left. They are effective in visualising the data & easy to read to show the relation between each of the attributes for the different flowers analysed and represented in the data set. They are generally developed from five statistic flowers from the data they are created to represent – the minimum, second quartile, the median, third quartile & the maximum, which relates to the values analysed and can be seen in the *.describe* output that will be mentioned later. However, it is widely known that while this box plot representation of the data can indicate the symmetry of a data set it is unable to indicate the shape of the data’s symmetry to the same level as a histogram [15][16].

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/siex2em77/Box_Plots.png" alt="Box_Plots"/></a><br/><br/>

 **- H) Area plot for all 4 attributes:**
 
 <a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/6vzwld877/Area_all_in_one_image_individually.jpg" alt="Area_all_in_one_image_individually"/></a><br/><br/> [14]
 
The area plot, represented on lines 70 through 73 in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), provide a visual output of line segments for each of the attributes represented in the dataset compared with each other. The plot showcases the magnitude difference between the values for the range of samples for each attribute & provides a comparison between the four columns. This was used as an alternate visual representation of the dataset attribute values and the trends between the attribute values measured in the dataset at a quick glance to a viewer looking through the analysis completed. For the purpose of this analysis the attribute values have been represented with stacked data plots rather than overlapping data points as it they are much easier to view and read. Any fluctuations to the values of the attributes can be clearly seen using the area graph while being able to also view whether or not the dataset contains consistant values for any of the attributes, therefore providing another view on any trends within the data set. One advantage of using the area chart for additional information over the line plot is the fact the filling between the line segments can assist in understanding the magnitude of the data for each of the attributes included in this dataset [17].

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/546xqhbzn/Area_Plot.png" alt="Area_Plot"/></a><br/><br/>
 
**- I) Scatter Matrix all 4 attributes:**

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/ixvafgrpf/Sctter_Matrix.jpg" alt="Sctter_Matrix"/></a><br/><br/> [5]

The code represented on lines 75 through 78 in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py) output a scatter matrix of all four attributes represented in the iris flower data set. Similar to previous analysis completed for this project it is a very useful statistical method of analysing data. The scatter matrix was produced for the purpose of this project to display any correlation between the attributes & have been produced as a matrix to ensure easy viewing of any correlations present. It includes various graph types with all attributes represented to ensure comparisons are possible within one figure. Such graphical representation of the data set is very useful when analysing data sets to explore any relationships between the attributes measured and as such was included for this analysis [18].
 
<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/om1l6ee2b/Scatter_Matrix.png" alt="Scatter_Matrix"/></a><br/><br/>

**- J) .describe function:** 

<a href="https://postimages.org/" target="_blank"><img src="https://s19.postimg.cc/qduk19uub/describe.jpg" alt="describe"/></a><br/><br/> [5]

The *.describe* section in [final.py](https://github.com/ShaunaB93/Iris-Data-Analysis-Project/blob/master/Final.py), represented on line 80 of the commit, was used as a suggestion for calculating some of the values represented in the function discussed previously. It was included as a suggested as it requires less code to produce the values & provides a display table of detailed distribution information for each of the 4 attributes represented within the data set, specifically providing the count, mean, standard deviation, minimum, maximum, 25th, 50th & 75th percentiles. The relevance of the values have been mentioned when previously calculated earlier in the script [5].

<a href='https://postimg.cc/image/k1fera75r/' target='_blank'><img src='https://s19.postimg.cc/k1fera75r/describe_output.jpg' border='0' alt='describe_output'/></a>

### Conclusion –
As the iris flower data set [1] is so well known there have been many projects completed using the data, especially for statistical analysis and machine learning, which have been published online.
From my own analysis it could be quickly determined that the petal measurements attributes are quite skewed through the visual outputs, while the sepal measurements appear quite symmetric. As mentioned previously, the histograms are the clearest evidence of the shape of the data related to the attributes in this case. However, as some of the data appears skewed it would represent that the petal attribute values appear to have a greater variance of values within the sample than the sepal related values appeared to show. While the scatter matrix allows for the most complex representation & comparison of the data measured of the four attributes of the flowers within the sample. The scatter matrix visual output shows that there is a diagonal grouping of some pairs of the attributes contained within the data set & this would suggest a predictable relationship between such attributes. I believe this is why many projects for learning how to create models for machine learning utilise this data set as it functions and proves that such algorithms can predict certain outcomes if trained correctly. 

The analysis completed in this case was based more so on statistical calculations related to the data set provided in order to obtain a greater view of the dataset & to provide visualisation of the results of the analysis conducted. However, in most projects completed the analysis is broadened to creating a machine learning tool from this dataset, such as predicting which flower class a set of measurements would belong to if provided to the algorithm. I found this quite interesting to research further into & found the iris flower data set was quite useful for creating such projects earlier due to its size. The accuracy & how to test such models were quite complex and would require further analysis but I based my statistical approach to this project on such projects as the basis for the creation of the models seemed to be based on the calculations & graphical representations that can be seen in the above code. One instance I have found can be seen under reference [20] or [21] below. However, it was also noted that the understanding of the data provided from completing the statistical analysis further assists in choosing the correct machine learning model but the accuracy should always be tested before relying on a model for 100% accuracy. While researching the background information into using the iris flower data set as a machine learning project was interesting there were certain aspects which I would like to develop my knowledge further in to in order to include such predictive analysis into future projects. If completing this project again this would be one area I would like to work further towards having an understanding of coding myself in order to have a more well-rounded predictive analysis by furthering the statistical analysis completed for this project. 

### References –
**- [1]** [https://archive.ics.uci.edu/ml/datasets/iris]
**- [2]** [https://statistics.laerd.com/statistical-guides/measures-central-tendency-mean-mode-median.php]
**- [3]** [https://www.researchconnections.org/childcare/datamethods/descriptivestats.jsp]
**- [4]** [https://www.researchconnections.org/childcare/research-glossary#M]
**- [5]** [https://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/]
**- [6]** [http://www.nedarc.org/statisticalHelp/basicStatistics/minAndMax.html]
**- [7]** [https://www.researchconnections.org/childcare/datamethods/descriptivestats.jsp]
**- [8]** [https://statistics.laerd.com/statistical-guides/understanding-histograms.php]
**- [9]** [https://statistics.laerd.com/statistical-guides/measures-of-spread-standard-deviation.php]
**- [10]** [https://plotlyblog.tumblr.com/post/118355223592/how-to-analyze-data-eight-useful-ways-you-can]
**- [11]** [https://matplotlib.org/users/pyplot_tutorial.html]
**- [12]** [http://howtothink.readthedocs.io/en/latest/PvL_H.html]
**- [13]** [https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/]
**- [14]** [https://data-lessons.github.io/library-python/06a-plotting-with-pandas/]
**- [15]** [http://asq.org/learn-about-quality/data-collection-analysis-tools/overview/box-whisker-plot.html]
**- [16]** [http://www.dummies.com/education/math/statistics/what-a-boxplot-can-tell-you-about-a-statistical-data-set/]
**- [17]** [https://www.fusioncharts.com/chart-primers/area-chart/]
**- [18]** [http://junkcharts.typepad.com/junk_charts/2010/06/the-scatterplot-matrix-a-great-tool.html]
**- [19]** [http://web.archive.org/web/20120313180502/http://www.le.ac.uk/biology/gat/virtualfc/Stats/descrip.html]
**- [20]** [https://analyticsindiamag.com/start-building-first-machine-learning-project-famous-dataset/]
**- [21]** [http://www.codeastar.com/beginner-data-science-tutorial/]
