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

matplotlib.use('Qt5Agg')  # библиотека для вывода графиков на базе Qt5, нужен импорт модуля PyQt5
# модуль печати плоских графиков
import matplotlib.pyplot as plt

plt.style.use('bmh')  # можно попробовать также 'ggplot' или 'classic'
fig = plt.figure()  # поверхность для вывода графиков (в виде всплывающего окна)

def mandelbrot( h,w, maxit=20 ):
     """Returns an image of the Mandelbrot fractal of size (h,w)."""
     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
     c = x+y*1j
     z = c
     divtime = maxit + np.zeros(z.shape, dtype=int)

     for i in range(maxit):
         z = z**2 + c
         diverge = z*np.conj(z) > 2**2            # who is diverging
         div_now = diverge & (divtime==maxit)  # who is diverging now
         divtime[div_now] = i                  # note when
         z[diverge] = 2                        # avoid diverging too much

     return divtime
plt.imshow(mandelbrot(400,400))
plt.show()

