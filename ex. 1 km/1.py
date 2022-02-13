import matplotlib.pyplot as plt
import random

r = float(input())
x0 = random.random()
a = []
n = 60
a.append(x0)
for i in range (1, n):
    a.append(4*r*a[i-1]*(1-a[i-1]))
plt.plot(range(n), a)

plt.show()