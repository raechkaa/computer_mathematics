import matplotlib.pyplot as plt
from random import random


# N=1000
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


N_list = [x for x in range(100,10000,100)]
res = []
for N in N_list:
    Pr0, Ill0 = draw_pc(100, 50, 3)
    for x in range(len(Ill0)):
        if Ill0[x] != 0:
            res.append(Pr0[x - 1])
            print(Pr0[x - 1])
            break
plt.plot(N_list, res)
plt.show()
