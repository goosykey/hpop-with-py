from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
from scipy import integrate
import numpy as np
from fun import *


def exponential_decay(t, y): return -0.5 * y


sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])
res = solve_ivp(funky_fun, (0, 10), np.array([50, 25]), max_step = 0.1)

print(res.t)
print(res.y)

plt.figure()
plt.plot(res.t, res.y[0, :])

plt.show()