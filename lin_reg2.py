"""
Author: Samarkin
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

import read_x_file

df = read_x_file.read_data('x01.txt')

df.hist([df.columns[1],df.columns[2]])
plt.show()

plt.scatter(df.iloc[:,1].values,df.iloc[:,2].values)
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

rho = df.corr(method='pearson')
print(rho)

# модель линейной регрессии
model = LinearRegression()
# формируем правильные массивы
length = len(df.iloc[:,1].values)
x = df.iloc[:,1].values.reshape(length,1)
y = df.iloc[:,1].values.reshape(length,1)
# строим модель (подгоняем коэффициенты)
model.fit(x,y)
print(model)
print(model.coef_)
print(model.intercept_)

# строим графики
plt.scatter(x, y,  color='black')
plt.plot(x, model.predict(x), color='blue', linewidth=1)
plt.xticks(())
plt.yticks(())
plt.show()