"""
Author: Самаркин А.И.
Date: 26/10/19
Purpose: test
"""

# стандартная секция импорта, будет использоваться всегда
# модули числовых расчетов
import scipy as sc
import numpy as np
import pandas as pd
# модуль библиотеки для вывода графиков в стиле Matlab
import matplotlib

matplotlib.use('Qt5Agg', force=True)  # библиотека для вывода графиков на базе Qt5, нужен импорт модуля PyQt5
# модуль печати плоских графиков
import matplotlib.pyplot as plt

plt.style.use('bmh')  # можно попробовать также 'ggplot' или 'classic'

# обратите внимание
# fig - собственно окно
# ax - в терминологии Ecell - область построения диаграммы, оси координат графика
# именно  ax задает такие свойства, как заголовок, например
fig, ax = plt.subplots()

delta = 0.0025
maxx = 2.0
maxy = 2.0
x = np.arange(-maxx, maxx, delta)
y = np.arange(-maxy, maxy, delta)
# сетка - массив на которм строится трехмерный график
X, Y = np.meshgrid(x, y)
# расчет Z
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
# расчет линий контура и печать
CS = ax.contour(X, Y, Z)
# вывод меток
ax.clabel(CS, inline=1, fontsize=8)

plt.show()


