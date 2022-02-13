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


generate(0.006, 10)


def draw(p, count):
    days = [i for i in range(count)]
    illness = generate(p, count)
    plt.plot(days, illness, linewidth=3, c='b')
    plt.show()


draw(0.6, 100)
