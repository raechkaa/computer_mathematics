import random
import math
from scipy import integrate

N = 1000
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
sigma = math.fabs(float(area_monte) - J_1) / J_1
print(sigma)
print(J_1)
print(float(area_monte))
