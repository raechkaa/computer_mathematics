import math
from matplotlib import pyplot as plt
import numpy as np

# method Эйлера
m = 0.06
g = 10
l = 0.1
tao = 0.03
N = 1000
x0 = 2
v0 = 0
def en(x,v):
    return m*(l**2)*((v**2)/2 + g*(1-math.cos(x))/l)

def f(x):
    return -g*math.sin(x)/l

V = [v0]
X = [x0]
T = [0]
E = [en(x0, v0)]
time = []
mth = []
for i in range(N):
    v = V[-1]
    x = X[-1]
    t = T[-1]
    V.append(v + tao * f(x))
    X.append(x + tao * v)
    T.append(t + tao)
    E.append(en(X[-1], V[-1]))

# Метод «предиктор-корректор»
V_ = [v0]
X_ = [x0]
T_ = [0]
E_ = [en(x0, v0)]
for i in range(N):
    v = V_[-1]
    x = X_[-1]
    t = T_[-1]
    v_ = v + tao * f(x)
    x_ = x + tao * v
    V_.append(v + tao * (f(x_) + f(x))/2)
    X_.append(x + tao * (v + v_)/2)
    T_.append(t + tao)
    E_.append(en(X_[-1], V_[-1]))

# Метод Эйлера-Кромера

W = math.sqrt(g/l)
t1 = np.linspace(0, 25, 1000)

v1 = lambda v_l, x_l, t4: v_l -(W**2)*math.sin(x_l)*t4
x1 = lambda v_l, x_l, t4: x_l + v_l * t4

def get_vt_xt(t):
    vt = [v1(0, x0, t1[0])]
    xt = [x0]
    len_t = len(t1)
    for i in range(1, len_t):
        delta_t = t1[i] -t1[i-1]
        v_i = v1(vt[i-1], xt[i-1], delta_t)
        x_i = x1(v_i, xt[i-1], delta_t)
        vt.append(v_i)
        xt.append(x_i)
    return vt, xt


vt, xt = get_vt_xt(t1)

E1 = [en(x0, v0)]
for i in range(1, len(vt)):
    E1.append(en(xt[i], vt[i]))

time = [T, T_, t1]
mth = [E, E_, E1]

plt.xlabel('t')
plt.ylabel('E(t)')
plt.plot(time[0], mth[0], color='green')  # method Эйлера
plt.plot(time[1], mth[1], color = 'red')  # Метод «предиктор-корректор»
plt.plot(time[2], mth[2], color='blue')  # Метод Эйлера-Кромера
plt.axhline(y=0.085, color='orange', linestyle='-')
plt.show()