import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import quandl as ql

import urllib3
from bs4 import BeautifulSoup



#a lists of equal sizes
web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

#lists converted to columns
df = pd.DataFrame(web_stats)

#set index using the day index
df.set_index('Day', inplace=True)
df['Visitors'].plot()
df.plot()
plt.show()

#import new data
data = pd.read_csv("C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/ZILL-Z77006_3B.csv", sep=',')
data.set_index('Date', inplace=True)

data.to_csv('newcv2.csv')

data2 = pd.read_csv("C:/Users/Serkan/PycharmProjects/panda/newcv2.csv", sep=",", index_col=0)

#quandl data
fifty = ql.get("FMAC/HPI_TX", authtoken='VqZcWGrZZ1fAYsTkUK6E')
fifty_state = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
