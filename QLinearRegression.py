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
fig = plt.figure()  # поверхность для вывода графиков (в виде всплывающего окна)

def HistAndScatter(df:pd.DataFrame,x_index:int,y_index:int):
    df.hist([df.columns[1], df.columns[2]])
    plt.show()

    plt.scatter(df.iloc[:, 1].values, df.iloc[:, 2].values)
    plt.show()
    pass

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def PandasToValues(df:pd.DataFrame,index:int):
    return df.iloc[:,index].values

def ValuesToData(values):
    return values.reshape(len(values), 1)

def PandasToData(df:pd.DataFrame,index:int):
    return ValuesToData(PandasToValues(df,index))

def PandasToXY(df:pd.DataFrame,x_index:int,y_index:int):
    return [PandasToData(df,x_index),PandasToData(df,y_index)]

def LinRegModel(df:pd.DataFrame,x_index:int,y_index:int, print_result = False):
    # модель линейной регрессии
    model = LinearRegression()
    # формируем правильные массивы
    # length = len(df.iloc[:, x_index].values)
    # x = df.iloc[:, x_index].values.reshape(length, 1)
    # y = df.iloc[:, y_index].values.reshape(length, 1)
    x = PandasToData(df,x_index);
    y = PandasToData(df,y_index);
    # строим модель (подгоняем коэффициенты)
    model.fit(x, y)
    if(print_result):
        print(model)
        print(model.coef_)
        print(model.intercept_)

    return model


