import matplotlib.pyplot as plt
import numpy as np


p_c = np.array([0.00001, 0.000015, 0.000026, 0.00006, 0.00016, 0.0002, 0.00025, 0.0009])
N = np.array([100000, 70000, 50000, 20000, 10000, 7000, 5000, 1000])
ln_p_c = np.log(p_c)
ln_N = np.log(N)
p_c_1 = 1/N
ln_p_c_1 = np.log(p_c_1)
plt.plot(ln_p_c, ln_N, 'bo')
plt.plot(ln_p_c_1, ln_N,'ro', color="green")
plt.show()
