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
# полярная проекция
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))

# создаем массив x
x = np.linspace(0,100,10000)
# рассчитываем y
y1 = np.sin(x)*np.exp(0.1*x)
y2 = np.sin(x)*np.exp(-0.1*x)

ax1.plot(x, y1)
ax2.plot(x, y2)

# Общий (супер) заголовок - он относится ко всему окну
fig.suptitle('Общий заголовок')


plt.show()


