import matplotlib.pyplot as plt
import numpy as np
import math
x0 = 5
def get_n_element(x0, r, n):
    f = lambda x: x*math.exp(r*(1-x))
    last = f(x0)
    for i in range(1, n):
        last = f(last)
    return last

r = np.concatenate((np.linspace(0, 3, 1000), np.linspace(3, 3.5, 1000)))
last = get_n_element(x0, r[0],1000)
xs = list()
i = 1
n = 10**3

xs = []
for _r in r:
    xs.append(get_n_element(x0, _r, n))
    n += 1

plt.plot(r, xs, "ro", markersize=0.5)
plt.show()
