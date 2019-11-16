"""
Author: Самаркин
Date: 
Purpose: test
"""

# стандартная секция импорта, будет использоваться всегда
# модули числовых расчетов
import scipy as sc
import numpy as np
import pandas as pd
# модуль библиотеки для вывода графиков в стиле Matlab
import matplotlib

# matplotlib.use('Qt5Agg')  # библиотека для вывода графиков на базе Qt5, нужен импорт модуля PyQt5
# модуль печати плоских графиков
import matplotlib.pyplot as plt

plt.style.use('bmh')  # можно попробовать также 'ggplot' или 'classic'
fig = plt.figure()  # поверхность для вывода графиков (в виде всплывающего окна)

import requests as r

data_url = "https://apps.who.int/gho/athena/data/GHO/MORT_100?filter=MGHEREG:WORLD;MGHEREG:REG6_AFR;MGHEREG:REG6_AMR;MGHEREG:REG6_EMR;MGHEREG:REG6_EUR;MGHEREG:REG6_SEAR;MGHEREG:REG6_WPR;CHILDCAUSE:CH8&x-sideaxis=MGHEREG;YEAR&x-topaxis=GHO;CHILDCAUSE;AGEGROUP&profile=crosstable&format=csv"
local_file = "data.csv"

res = r.request(url=data_url,method='Get')
data = res.text
data = data.replace('"','')
print(data)

f = open(local_file,'w')
f.writelines(data)
f.close()

df = pd.read_csv(local_file,header=2)
print(df.columns)

regions = df.iloc[:,0].values
years = df.iloc[:,1].values
days27=df.iloc[:,2].values
monts59=df.iloc[:,3].values
years4=df.iloc[:,4].values

fig = plt.figure()
plt.hist(monts59)
plt.show()

fig = plt.figure()
plt.plot(monts59)
plt.show()

print('Sum of %g'%np.sum(monts59))
print('Mean of %g'%np.mean(monts59))
print('Median of %g'%np.median(monts59))
print('Variance of %g'%np.var(monts59))
print('Std dev of %g'%np.std(monts59))

fig = plt.figure()
plt.boxplot(monts59)
plt.show()

print('Sum of %g'%np.sum(years4))
print('Mean of %g'%np.mean(years4))
print('Median of %g'%np.median(years4))
print('Variance of %g'%np.var(years4))
print('Std dev of %g'%np.std(years4))

print(df.columns)

