import numpy as np


data_array = np.genfromtxt('data.txt', delimiter=',')

x=2
np.mean(data_array.reshape(-1, x), 1)

np.savetxt('avgdata.dat', dat, delimiter=" ", fmt="%15.10f")
