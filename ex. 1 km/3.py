import matplotlib.pyplot as plt
import random

n = 1000
R = []
for k in range(1, 1000):
    x0 = random.random()
    a = []
    a.append(x0)
    r = 0.001*k
    for i in range(1, n):
        a.append(4*r*a[i-1]*(1-a[i-1]))
    plt.scatter([r]*50, y=a[950:], s=0.5, color='green')
plt.show()
