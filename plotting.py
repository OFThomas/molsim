#!/bin/bash 

import matplotlib.pyplot as plt
import numpy as np

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)

plt.plot(temp, u, 'o')
plt.errorbar(temp, u, yerr=uerr, xerr=temperr, fmt='o')
plt.show()
