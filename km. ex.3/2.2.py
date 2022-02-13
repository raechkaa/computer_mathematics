import matplotlib.pyplot as plt
import random


N = 1000


def generate(p, count):
    ill = [1]
    for i in range(1, count):
        n = ill[-1]
        z = N - n

        illness = 0
        for person in range(z):
            P = 1 - (1 - p) ** n
            r = random.random()
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
            plt.plot(days, illness_i, linewidth=1, color=(random.random(), random.random(), random.random()))
        for j in range(count):
            illness[j] += illness_i[j]/avg
    return illness


def draw_avg(p, count, avg, draw_avg=False):
    days = [i for i in range(count)]
    illness = generate_avg(p, count, avg, draw_avg)
    plt.plot(days, illness, linewidth=3, c='b')
    plt.show()


draw_avg(0.006, 10, 10, True)
draw_avg(0.006, 10, 10)
