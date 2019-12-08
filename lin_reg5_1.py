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
fig, ax = plt.subplots()  # поверхность для вывода графиков (в виде всплывающего окна)

# создаем массив x
x = np.linspace(0,100,10000)
# рассчитываем y
y = np.sin(x)*np.exp(-0.01*x)

# печатаем заголовок
ax.set_title('Просто заголовок')
# график
ax.plot(x,y)
plt.show()


