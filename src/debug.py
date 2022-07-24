from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

x= range(2,26,2)
y= [15,13,14,5,17,21,23,25,28,30,25,19]
# plt.plot(x,y)
# plt.show()

data_dict = {
    'name':['David','Tim','Tom'],
    'age':[22,27,34],
}

pandas_df = pd.DataFrame(data_dict)
print(pandas_df)

df01=pd.DataFrame(columns=['age','score'])
df01['score']=np.random.randint(50,100,size=(10))
df01['age']=np.random.randint(20,35,size=(10))
df01.plot(x='age',y='score',kind='scatter')
print(df01)
print(df01.sort_values(by=['age']))
sorted_df02 = df01.sort_values(by=['age'])
sorted_df02.plot(x='age',y='score')

data_url = "https://github.com/turingplanet/pandas-intro/blob/main/public-datasets/iris.csv"
iris_data_df = pd.read_csv(data_url)
print(iris_data_df)
