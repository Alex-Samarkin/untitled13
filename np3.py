"""
Author: 
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

matplotlib.use('TkAgg')  # библиотека для вывода графиков на базе Qt5, нужен импорт модуля PyQt5
# модуль печати плоских графиков
import matplotlib.pyplot as plt

plt.style.use('bmh')  # можно попробовать также 'ggplot' или 'classic'
fig = plt.figure()  # поверхность для вывода графиков (в виде всплывающего окна)

a=np.arange(10)
print(a)

b=np.arange(1,5)
print(b)

c=np.arange(0.0,10.0,0.25)
print(c)

d=np.linspace(0,10,1000)
print(d)

e = np.random.random([20])
print(e)

f = np.random.normal(0.0,1.0,200)
print(f)

