import matplotlib.pyplot as plt
from random import random
import math
from tqdm import tqdm

N = 1000


def gen(p, c):
    sick = [1]
    for i in range(1, c):
        today = sick[-1]
        healthy = N - today
        sickness = 0
        for ch in range(healthy):
            Ph_s = 1 - (1 - p) ** today
            r = random()
            if r < Ph_s:
                sickness += 1
        sick.append(sickness)
    return sick


def f(p, count, avg, graf=False):
    illness = [0 for i in range(count)]
    days = [i for i in range(count)]
    for i in range(avg):
        illness_i = gen(p, count)
        if graf:
            plt.plot(days, illness_i, linewidth=1, color=(random(), random(), random()))
        for j in range(count):
            illness[j] += illness_i[j]/avg
    return illness


def draw_predel(prob, count, avg, is_d=True):
    #Pr = [i/prob/1000*2 for i in range(prob)]
    Pr = [i/prob for i in range(prob)]
    Ill = []
    for i in tqdm(range(prob)):
        p = Pr[i]
        n1, n2 = f(p, count, avg)[-2:]
        n = n1 / 2 + n2 / 2
        Ill.append(n)
    if is_d:
        plt.plot(Pr, Ill, c='r')
        plt.show()
    return Pr, Ill


Pr_, Ill_ = draw_predel(100, 100, 100)

