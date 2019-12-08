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
# fig = plt.figure()  # поверхность для вывода графиков (в виде всплывающего окна)

import statsmodels.api as sm
import statsmodels.formula.api as smf

dat = sm.datasets.get_rdataset("Guerry", "HistData").data
print(dat.columns)

results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()

fig,(ax1,ax2) = plt.subplots(2,1)
ax1.plot(np.log(dat['Pop1831']))
ax2.plot(dat['Literacy'])
plt.show()

fig,(ax1,ax2) = plt.subplots(2,1)
ax1.plot(np.log(dat['Pop1831']),dat['Lottery'])
ax2.plot(dat['Literacy'],dat['Lottery'])
plt.show()

plt.plot(dat['Lottery'],dat['Literacy'],dat['Pop1831'])
plt.show()

spector_data = sm.datasets.spector.load(as_pandas=False)
spector_data.exog = sm.add_constant(spector_data.exog, prepend=False)

# Fit and summarize OLS model
mod = sm.OLS(spector_data.endog, spector_data.exog)
res = mod.fit()

print(res.summary())
