import matplotlib.pyplot as plt
import random
import math

n = 1000
R = []
step_1 = 0
for k in range(1, 1000):
    x0 = random.random()
    a = []
    a.append(x0)
    r = 0.003*k
    for i in range(1, n):
        a.append(a[i-1]*math.exp(r*(1-a[i-1])))
    for i in range(950, n - 2**step_1, 2**step_1):
        if round(a[i], 2) != round(a[i + 2**step_1], 2):
            print(r)
            R.append(r)
            step_1 += 1
            plt.scatter(r, a[i], s=0.5, color='yellow')
            break
    plt.scatter([r] * 50, y=a[950:], s=0.5, color='green')

for i in range(0, len(R)-3):
    print('delta', (R[i+1]-R[i])/(R[i+2]-R[i+1]))

plt.show()
