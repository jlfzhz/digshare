import pandas as pd
import numpy as np
from pathlib import Path
import os


data_url = os.path.join(Path(__file__).parents[1],'data','country.csv')
country_table=pd.read_csv(data_url,delimiter=',')
# print(country_table)

# df_country = country_table.set_index('Country', inplace=True)
# print(country_table[['Country','Region','Population','Climate']])
# print(country_table[['Country','Region','Population','Climate'=='1']])
# print(df_country)
# print(country_table.iloc[1:5,3])
# print(country_table.iloc[1])
# country_table.set_index('Country')
# print(country_table.index)
# country_table.set_index('Country', inplace=True)
# print(country_table)
# print(country_table.loc['China',['Climate','Birthrate','Deathrate']])


climate_filter = (country_table['Climate'] == '1')
f1 = country_table.loc[climate_filter, ['Country','Population','Climate']]
# print(f1.sort_values(by=['Country','Climate'],ascending=[False,True]))

print(country_table.sort_values(by=['Climate','Population','Country']))