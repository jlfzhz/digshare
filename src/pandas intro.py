import numpy as np
import pandas as pd

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


country_data = pd.read_csv(".//data//country.csv")
print(data_series)
print(country_data)
