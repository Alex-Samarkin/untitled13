

import scipy as sc
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('bmh')

fig = plt.figure()

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

print(ts)
plt.show()