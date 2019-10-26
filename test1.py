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
matplotlib.use('Qt5Agg') # библиотека для вывода графиков на базе Qt5, нужен импорт модуля PyQt5
# модуль печати плоских графиков
import matplotlib.pyplot as plt
print(plt.style.available) # печать доступных стилей вывода
plt.style.use('bmh') # можно попробовать также 'ggplot' или 'classic'

fig = plt.figure() # поверхность для вывода графиков (в виде всплывающего окна)

# тест модуля pandas
# серия случайных чисел
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# подсчет накопленной суммы
ts = ts.cumsum()
# печать на скрытой от пользователя поверхности
ts.plot()
# печать серии в командной строке
print(ts)
# вывод графика для пользователя
plt.show()