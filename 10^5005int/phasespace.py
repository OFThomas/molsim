#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt

k = np.genfromtxt('prod_100.tup', usecols=[2], unpack=True)
posx, posy, posz = np.genfromtxt('prod_100.out', unpack=True)
pos=np.sqrt(posx**2+posy**2+posz**2)

plt.plot(pos, k, 'o')

plt.show()
