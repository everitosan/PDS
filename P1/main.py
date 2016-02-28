import matplotlib.pyplot as plt
import numpy as np
from math import *


fo = float(1000)
fs = (2*fo)
x = []

y = np.arange(0, 0.1, 1/fs)

for i in y:
    mult = 700*2*pi*i
    xStep = sin(mult)
    x.append(xStep)

plt.plot(x)
plt.show()

