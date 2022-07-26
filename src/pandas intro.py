import numpy as np
import pandas as pd
import os
import pathlib

random_int = np.random.randint(50,100,size=(10))

print(random_int)

series01 = pd.Series(random_int)

print(series01)

print(series01[0])
print(series01[9])


data_dict = {'a':1, 'b':2, 'c':8}
data_series = pd.Series(data_dict, name='list')
print(data_series)
data_series=data_series.rename('new list')
print(data_series)

# print(os.path.dirname(os.getcwd()))
# print(os.getcwd())
# print(os.path.curdir)
# print(os.path.split(os.path.abspath(__file__)))
# print(os.path.pardir(os.path.abspath(__file__)))
# print(type(os.path.abspath(__file__)))
print(pathlib.Path(__file__).parents[1])
data_url = os.path.join(pathlib.Path(__file__).parents[1],'data','country.csv')
country_table=pd.read_csv(data_url,delimiter=',')
# print(country_table)
print(country_table.iloc[100])