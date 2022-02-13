import random
import math
from scipy import integrate
import matplotlib.pyplot as plt
from numpy import polyfit, poly1d


average = []
quantity_N = []

for j in range(1000, 10000, 500):
    sum_sigma = 0
    rep = 100
    N = j
    quantity_N.append(math.log(N))
    for i in range(rep):
        success = 0
        J = integrate.quad(lambda x: math.sin(x), 0, math.pi)
        J_1 = float(J[0])

        for i in range(N):
            x1 = random.uniform(0, math.pi)
            y1 = random.uniform(0, 1)
            value = math.sin(x1)
            if y1 <= value:
                success += 1

        area_total = 1 * math.pi
        area_monte = area_total * success / N

        sigma = math.fabs(area_monte - J_1) / J_1
        sum_sigma += sigma

    average_sigma = sum_sigma / rep
    average.append(math.log(average_sigma))

alpha = average[0]/quantity_N[0]
print(alpha)
coeff = polyfit(average, quantity_N, 1)
p = poly1d(coeff)
plt.plot(average, quantity_N)
plt.scatter(average, p(quantity_N))
plt.show()
