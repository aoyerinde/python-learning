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

#O cos its html, 1- column  1
#print column 1 od df o and attach it to a string
for abbv in fifty_state[0][1][1:]:
    print("FMAC/HMI_"+ str(abbv))

df1 = pd.DataFrame({'HPI':[80,85,88,85],'Int_rate':[2,3,2,2],'US_GDP_Thousands':[50,55,65,55]}, index=[2001,2002,2003,2004])
df2 = pd.DataFrame({'HPI':[80,85,88,85],'Int_rate':[2,3,2,2],'US_GDP_Thousands':[50,55,65,55]}, index=[2005,2006,2007,2008])
df3 = pd.DataFrame({'HPI':[80,85,88,85],'Int_rate':[2,3,2,2],'Low_tier_HPI':[50,52,50,53]}, index=[2001,2002,2003,2004])

concat = pd.concat([df1,df2])
concat = pd.concat([df1,df2,df3])
df4 = df1.append(df3)

#append or  concat, appent only if columns match

s = pd.Series ([80,2,50], index=['HPI','Int_rate', 'US_GDP_Thousands'])
df5 = df1.append(s, ignore_index = True)

#append and ignore index

df3 = pd.DataFrame({'HPI':[80,85,88,85],'Unemployment':[7,8,9,6],'Low_tier_HPI':[50,52,50,53]}, index=[2001,2002,2003,2004])

#like joins

join = pd.merge(df1, df3, on='HPI')
join.set_index('HPI', inplace = True)

#left joinn

merged = pd.merge(df1, df2, on='US_GDP_Thousands', how = 'left')

#
main = pd.DataFrame()
for abbv in fifty_state[0][0][1:]:
    query = "FMAC/HPI_"+ str(abbv)
    ef = ql.get(query, authtoken='tA7fEB9j5E52dEcSXGDS')

    if main.empty:
      main = ef
    else:
      main = main.join(ef)
