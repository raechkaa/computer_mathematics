import matplotlib.pyplot as plt
import random

r = 0.91
x01 = 0.50
x02 = 0.50
a = []
b = []
n = 180
a.append(x01)
for i in range(1, n):
    a.append(4*r*a[i-1]*(1-a[i-1]))
b.append(x02)
for i in range(1, n):
    # b[i - 1] = b[i - 1] / 10
    # b[i - 1] = b[i - 1] * 10
    # b[i - 1] = b[i - 1] / 16
    # b[i - 1] = b[i - 1] * 16
    # b[i - 1] = b[i - 1] / 20
    # b[i - 1] = b[i - 1] * 20
    b.append(4*r*b[i-1]*(1-b[i-1]))
plt.plot(range(n), a, color='red')
plt.plot(range(n), b, color='black')
plt.show()
