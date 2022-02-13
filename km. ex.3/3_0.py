import matplotlib.pyplot as plt
from random import random
import math
from tqdm import tqdm


N = 1000


def generate(p, count):
    ill = [1]
    for i in range(1, count):
        # число заболевших сегодня
        n = ill[-1]
        # число здоровых
        z = N - n

        illness = 0
        for person in range(z):
            # вероятность что здоровый человек заболеет
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
            plt.plot(days, illness_i, linewidth=1, color=(blue, green, yellow))
        for j in range(count):
            illness[j] += illness_i[j] / avg
    return illness


def draw_predel(prob, count, avg, is_d=True):
    Pr = [i / prob / 1000 * 3 for i in range(prob)]
    # Pr = [i/prob for i in range(prob)]
    Ill = []
    for i in tqdm(range(prob)):
        p = Pr[i]
        n1, n2 = generate_avg(p, count, avg)[-2:]
        n = n1 / 2 + n2 / 2
        Ill.append(n)
    if is_d:
        plt.plot(Pr, Ill, c='b')
        plt.show()
    return Pr, Ill


Pr_, Ill_ = draw_predel(100, 100, 100)
p_c = 0.001055
p_c_analit = 1 - math.exp(-1 / 1000)
print('p_c_analit=', p_c_analit)
p_c_analit = 0.000999500166624978
