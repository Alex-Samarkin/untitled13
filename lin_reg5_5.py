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
# ДВА*ДВА - сетка подграфика на одной поверхности но по горизонтали
fig, ax = plt.subplots(2,2)  # поверхность для вывода графиков (в виде всплывающего окна)

# создаем массив x
x = np.linspace(0,100,10000)
# рассчитываем y
y = np.sin(x)*np.exp(-0.01*x)

# график в первой ячейке
ax[0, 0].plot(x, y)
# заголовок
ax[0, 0].set_title('Axis [0,0]')
ax[0, 1].plot(x, y, 'tab:orange')
ax[0, 1].set_title('Axis [0,1]')
ax[1, 0].plot(x, -y, 'tab:green')
ax[1, 0].set_title('Axis [1,0]')
ax[1, 1].plot(x, -y, 'tab:red')
ax[1, 1].set_title('Axis [1,1]')

# заголовки по осям координат
for axs in ax.flat:
    axs.set(xlabel='x-label', ylabel='y-label')
# чтобы убрать промежуточные подписи по осям
for axs in ax.flat:
    axs.label_outer()


# Общий (супер) заголовок - он относится ко всему окну
fig.suptitle('Общий заголовок')


plt.show()


