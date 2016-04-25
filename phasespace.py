#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt

time, k = np.genfromtxt('prod_100.tup', usecols=[0,2], unpack=True)
#posx, posy, posz = np.genfromtxt('prod_100.out', unpack=True)
#pos=np.sqrt(posx**2+posy**2+posz**2)

plt.plot(time, k, 'o')

plt.show()
