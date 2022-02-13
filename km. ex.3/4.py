import numpy as np
import matplotlib.pyplot as plt
import time




def epidemic(p, num_of_sick, num_of_days, N):
    n = num_of_first_sick
    sick = np.array([0 for _ in range(num_of_days)])
    Days_array = np.array(range(num_of_days))
    sick[0] = num_of_first_sick
    for day in Days_array[1:]:
        if sick[day - 1] == 0 or sick[day - 1] == N:
            sick[day] = 0
        else:
            sum_p = 1 - (1 - p) ** n
            vals = np.random.uniform(0, 1, N - n)
            for _ in range(N - n):
                val = vals[_]
                if val < (sum_p):
                    sick[day] += 1
            n = sick[day]
    return sick



various_ep = 20
num_of_days = 20
num_of_first_sick = 1

prob1 = sorted(np.random.uniform(0, 0.001, 10))
prob2 = sorted(np.random.uniform(0.001, 0.004, 10))
prob_for_1000 = np.concatenate((prob1, prob2), axis=None)

time_s = time.time()
Epidemics = []
Epidemic_av_per_day = []
for p in prob_for_1000:
    Epidemic_p = np.array([epidemic(p, num_of_first_sick, num_of_days, 1000)
                           for i in range(various_ep)])
    Epidemics.append(Epidemic_p)
    Epidemic_av_per_day.append(np.average(Epidemic_p, axis=1))

print(time.time() - time_s)


Epidemic_av_per_day_10000 = []
Epidemic_av_per_day_100000 = []
Epidemics_10000 = []
Epidemics_100000 = []
prob1 = sorted(np.random.uniform(0, 0.0002, 17))
prob2 = sorted(np.random.uniform(0.0002, 0.0005, 3))
prob = np.concatenate((prob1, prob2), axis=None)
time_s = time.time()
for p in prob:
    Epidemic_p = [epidemic(p, num_of_first_sick, num_of_days, 10000)
                  for i in range(various_ep)]
    Epidemics_10000.append(Epidemic_p)
    Epidemic_av_per_day_10000.append(np.average(Epidemic_p, axis=1))

print(time.time() - time_s)

Epidemic_av_per_day_10000 = np.array(Epidemic_av_per_day_10000)
# print(Epidemic_av_per_day_10000)

# Epidemic_av_per_day_10000 = []
# Epidemic_av_per_day_100000 = []
# Epidemics_10000 = []
# Epidemics_100000 = []
# prob1 = sorted(np.random.uniform(0, 0.0002, 17))
# prob2 = sorted(np.random.uniform(0.0002, 0.0005, 3))
# prob = np.concatenate((prob1, prob2), axis = None)
time_s = time.time()
for p in prob:
    #     Epidemic_p = np.array([epidemic(p, num_of_first_sick, num_of_days, 10000)
    #                           for i in range(various_ep)])
    #     Epidemics_10000.append(Epidemic_p)
    #     Epidemic_av_per_day_10000.append(np.average(Epidemics_10000, axis=1))

    Epidemic_p = np.array([epidemic(p, num_of_first_sick, num_of_days, 100000)
                           for i in range(various_ep)])
    Epidemics_100000.append(Epidemic_p)
    Epidemic_av_per_day_100000.append(np.average(Epidemic_p, axis=1))

Epidemic_av_per_day_10000 = np.array(Epidemic_av_per_day_10000)
lim_num_of_sick_10000 = np.average(Epidemic_av_per_day_10000[:, -10:-1], axis=1)

Epidemic_av_per_day_100000 = np.array(Epidemic_av_per_day_100000)
lim_num_of_sick_100000 = np.average(Epidemic_av_per_day_100000[:, -10:-1], axis=1)

print(time.time() - time_s)
265.74753618240356
In[]:
Epidemic_av_per_day = np.array(Epidemic_av_per_day)
lim_num_of_sick_1000 = np.average(Epidemic_av_per_day[:, -10:-1], axis=1)
In[]:
lim_num_of_sick_rel_1000 = lim_num_of_sick_1000 / 1000
lim_num_of_sick_rel_10000 = lim_num_of_sick_10000 / 10000
lim_num_of_sick_rel_100000 = lim_num_of_sick_100000 / 100000

plt.plot(prob_for_1000, lim_num_of_sick_rel_1000, label='N=1 000', color="C0")
plt.plot(prob, lim_num_of_sick_rel_10000, label='N=10 000', color="b")
plt.plot(prob, lim_num_of_sick_rel_100000, label='N=100 000', color='g')
plt.legend()