import csv
import numpy as np
import pandas as pd
from time import time
from IPython.display import  display




import  matplotlib.pyplot as plt
import  seaborn as sns



data = pd.read_csv("C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/winequality-red.csv", sep=';')

display((data.head(n=5)))

#look for nulls

data.isnull().any()

#data info
data.info()

#consider wines with ratings 7 as very good and 5,6 as  average, basically tagging

n_wines = data.shape[0]

#winns with quality above 6

quality_above_6 = data.loc[(data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]


quality_below_5  = data.loc[(data['quality'] < 5)]
n_below_5 = quality_below_5 .shape[0]

quality_between_5 = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
n__between_5 = quality_between_5.shape[0]


#% of wines with quality above 6

greater_percent = n_above_6*100/n_wines

print("Total number of wines data : {}".format(n_wines))


display(np.round(data.describe())) #display stats on all the data


#witthin feature correlation
pd.plotting.scatter_matrix(data, alpha =0.3, figsize =(40,40), diagonal ='kde')

#then use heat map

correlation = data.corr()
#display it
plt.figure(figsize=(14,12)) #empty casket
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

#visualize corelation between two columns in a data frrame
#create a new data from from all to be able to pick out two

Fixed_acidity_ph = data[['pH', 'fixed acidity']]


#initialize a joint  grid with dt frame using seaborn

gridA = sns.JointGrid(x="fixed acidity", y="pH", data=Fixed_acidity_ph, size=6)

#regression plot in the gridA
gridA = gridA.plot_joint(sns.regplot, scatter_kws={"s":10})

#draw a distrobution  plot in same grid
gridA = gridA.plot_marginals(sns.distplot)

#fixec acidity vs citric acid

fixedacidity_citricacid = data[['citric acid', 'fixed acidity']]

g = sns.JointGrid(x="fixed acidity", y ="citric acid", data=fixedacidity_citricacid, size=6)
g = g.plot_joint(sns.regplot, scatter_kws={"s":10})
g = g.plot_marginals(sns.distplot)

#acidity vs quality in box plots

volatileAcidity_quality =  data[['volatile acidity','quality']]
fig, axs = plt.subplots(ncols=1,figsize =(10,6))
sns.barplot(x='quality', y='volatile acidity', data=volatileAcidity_quality, ax = axs)
plt.title('quality VS volatile acidity')

plt.tight_layout()
plt.show()
plt.gcf().clear()

#check alcohol vs quality

Alcohol_quality = data [['alcohol','quality']]

fig, axs = plt.subplots(ncols=1, figsize=(10,6))
sns.barplot(x='quality',y='alcohol', data= Alcohol_quality, ax = axs)
plt.title ('quality vs Alcohol')
plt.show()
plt.gcf().clear

#looking foor outliers

for feature in data.keys():
    #calc q1 of given feature i.e 25th percentile
    q1 = np.percentile(data[feature], q=25)
    q3 = np.percentile(data[feature], q=75)
    #use intr quartile range to calc outlier and step (1.5 time the interquartilr range)
    interquartile_range = q3-q1
    step = 1.5*interquartile_range

    #display the outliers
    print("Data point considered outliers for the feature '{}':".format(feature))
    display(data[~((data[feature] >= q1 - step) & (data [feature] <= q3 +step))])
    outlier =[]

#remove outliers

good_data = data.drop(data.index[outlier]).reset_index(drop =True)
