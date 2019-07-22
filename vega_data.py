from vega_datasets import  data
import  pandas as  pd

data.list_datasets()
flights = data.flights_2k()

row = next(flights.iterrows())[1]

for index, row  in flights.head(n=2).iterrows():
    print(index,row)

for index, row in flights.head().iterrows():
    print(index,row['delay'], row['distance'], row['origin'])
df = pd.DataFrame([[3,5.5]], columns=['int_col', 'float_col'])

row_2 = next(df.iterrows())[1]

print(row_2['int_col'].dtype)

#case 2

import numpy as np

data_url = 'http://bit.ly/2cLzoxH'
gapminder = pd.read_csv(data_url)

gapminder['lifeExp_ind'] = np.where(gapminder.lifeExp >= 50, True, False)
gapminder['gdpPercap_ind'] = gapminder.gdpPercap.apply(lambda x:1 if x >=1000 else 0)
