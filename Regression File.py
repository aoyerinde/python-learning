import numpy as np
import matplotlib.pylab as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array([15,32,66,45,90,153,170,200])

plt.scatter(x,y)

#slope

m =  (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y) )/  (len(x) * np.sum(x*x) - (np.sum(x)**2))
b = (np.sum(y) - m* np.sum((x))) / len (x)

def predict (x):
    return 27*x - 26

vec = np.arange(10)
plt.scatter(x,y)
plt.plot(vec, predict(vec))


def getlinear (x,y):
    def inner(x1):
        return m * x1 + b
    m =  (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y) )/  (len(x) * np.sum(x*x) - (np.sum(x)**2))
    b = (np.sum(y) - m* np.sum((x))) / len (x)
    return  inner

predict = getlinear(x,y)
y1 = predict(4)


plt.scatter(x,y)
plt.plot(y1, predict(y1))


#sql like

import pandas as pd

airports =  pd.read_csv('C:/Users/Serkan/PycharmProjects/panda/airports.csv')
airport_freq =  pd.read_csv('C:/Users/Serkan/PycharmProjects/panda/airport-frequencies.csv')
runways =  pd.read_csv('C:/Users/Serkan/PycharmProjects/panda/runways.csv')

#where
Klax = pd.DataFrame()

#sort
Klax = airports[airports.ident == 'KLAX'].sort_values('type', ascending= False)

#in..Not in

helli_ballon = airports[airports.type.isin(['heliport', 'balloonport'])]

#group

group_order = airports.groupby(['iso_country','type']).size()

group_order_2 = airports.groupby(['iso_country','type']).size().to_frame('size').reset_index().sort_values(['iso_country','size'], ascending=[True,False])

#having
having = airports[airports.iso_country == 'US'].groupby('type').filter(lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)

nlargest = by_country.nlargest(10, columns = 'airport_count')

runway_agg  =  runways.agg({'length_ft':['min','max','mean','median']})


# joins
airport_freq.merge(airports[airports.ident == 'KLAX'][['id']], left_on= 'airport_ref', right_on='id', how='inner') [['airport_ident','type', 'description','frequency_mhz']]


concat = pd.concat([airports[airports.ident == 'KLAX'][['name', 'municipality']],
                    airports[airports.ident == 'KLGB]'][['name', 'municipality']]])
#insert
df1 = pd.DataFrame({'id':[1,2], 'name':['harry','Ron']})

df2 =  pd.DataFrame({'id':[3], 'name':['hermione']})

df3 =  pd.concat([df1,df2]).reset_index(drop=True)

#update

airports.loc[airports['ident']=='KLAX', 'home_link'] = 'NXM'
