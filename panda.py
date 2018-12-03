import pandas as pd
import numpy as np


import matplotlib.pyplot as plt

np.random.seed(0)

s = pd.Series([1,3,5,np.nan,6,8])

#datafram
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=list('ABCD'))

#dataframe by passin a dict of objects
df2 = pd.DataFrame({ 'A' : 1.,
                    'B': pd.Timestamp('20130102'),
                     'C':pd.Series(1,index=list(range(4)), dtype='float32'),
                     'D': np.array([3]*4, dtype='int32'),
                     'E': pd.Categorical(['test','train','test','train']),
                     'F': 'foo'})
df.describe()
df.T
df.sort_values(by='B')
df['A']
df[0:3] #row

df['20130102':'20130103']#

df.loc[:,['A','B'], #locale, first all time: column select

df.loc['20130102':'20130103',['A','B']],

df.loc[dates[0], 'A'],

df.at[dates[0], 'A'],

#int slicing
df.iloc[[1,2,4],[0,2]] , #row position then column in a casket


df[df > 0],

df2 = df.copy();
df2['E'] = ['asd','fgh','hjk','klö','qwe','tzu'],

#search in
df2[df2['E'].isin(['fgh','tzu'])],


s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102',periods=6));

df['F'] = s1

df.iat[0,1]


