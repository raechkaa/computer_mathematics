import matplotlib.pyplot as plt
from random import random


def generate(p, count):
    ill = [1]
    for i in range(1, count):
        n = ill[-1]
        z = N - n

        illness = 0
        for person in range(z):
            P = 1 - (1 - p) ** n
            r = random()
            if r < P:
                illness += 1
        ill.append(illness)
    return ill


def generate_avg(p, count, avg, draw_avg=False):
    illness = [0 for i in range(count)]
    days = [i for i in range(count)]
    for i in range(avg):
        illness_i = generate(p, count)
        if draw_avg:
            plt.plot(days, illness_i, linewidth=1, color=(random(), random(), random()))
        for j in range(count):
            illness[j] += illness_i[j] / avg
    return illness


def draw_pc(prob, count, avg):
    Pr = [i / prob / 10000 * 3 for i in range(prob)]
    Ill = []
    for i in range(prob):
        p = Pr[i]
        n1, n2 = generate_avg(p, count, avg)[-2:]
        Ill.append(n1 / 2 + n2 / 2)

    plt.plot(Pr, Ill, color='b')
    # plt.show()
    return Pr, Ill


Pr_array = []
Ill_array = []
N_list = [100, 500, 1000, 10000, 50000]
for N in N_list:
    Pr0, Ill0 = draw_pc(50, 50, 3)
    print('N = ', N)
    Pr_array.append(Pr0)
    Ill_array.append(Ill0)

for i in range(len(Pr_array)):
     plt.plot(Pr_array[i], [x / N_list[i] for x in Ill_array[i]], color=(random(), random(), random()),label=str(N_list[i]))
# plt.legend()
# plt.show()
#N_list = [100, 300, 500, 700, 1000, 10, 30, 50, 70]
# for i in range(len(Pr_array)):
    # plt.plot(Pr_array[i], [x / N_list[i] for x in Ill_array[i]], color=(random(), random(), random()), label = str(N_list[i]))
# plt.legend()
plt.show()

