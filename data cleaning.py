import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/Serkan/PycharmProjects/panda/python-data-cleaning-master/python-data-cleaning-master/Datasets/BL-Flickr-Images-Book.csv')
df.head()

#drop shitty columns
to_drop = ['Edition Statement',
            'Corporate Author',
           'Corporate Contributors',
           'Former owner',
           'Engraver',
           'Contributors',
           'Issuance type',
           'Shelfmarks']

#make identifier as the index
df.drop(to_drop, inplace=True, axis=1)
df['Identifier'].is_unique


df = df.set_index('Identifier', inplace=True)
df.loc[206]

#get data tyes
df.get_dtype_counts()
df.loc[1905:, 'Date of Publication'].head(10)

#beat the year head to fit
#extract the first four strings
extr = df['Date of Publication'].str.extract(r'(\d{4})', expand = False)
extr.head(10)

#now convert data type and replace the columns
df['Date of Publication'] = pd.to_numeric(extr)
df['Date of Publication'].dtype

#calculate how many nulls in data set
df['Date of Publication'].isnull().sum()/len(df)
#string filter
df['Place of Publication'].head(10)

#use a boolean mask to remove the name
pub = df['Place of Publication']
london = pub.str.contains('London')
london[:5]

oxford = pub.str.contains('Oxford')

#combine them in where clause
df['Place of Publication'] = np.where(london, 'London', np.where(oxford, 'Oxford',\
                                                                 pub.str.replace('-','')))
#now move to data cleaning 2
university_town =[]
with open('C:/Users/Serkan/PycharmProjects/panda/python-data-cleaning-master/python-data-cleaning-master/Datasets/university_town.txt') as file:
    for line in file:
        if '[edit]' in line:
            # remember  zhis `state` unitl the next is found
           state = line
        else:
            #otherwise, we have to keep `state` as last-seen
            university_town.append((state, line))

