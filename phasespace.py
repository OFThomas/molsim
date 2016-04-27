#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt

blengtha, errora = np.genfromtxt('tempproda_100.txt', usecols=[0,1], unpack=True)
blengthb, errorb = np.genfromtxt('tempprodb_100.txt', usecols=[0,1], unpack=True)
blengthc, errorc = np.genfromtxt('tempprodc_100.txt', usecols=[0,1], unpack=True)


plt.plot(blengtha, errora, 'ro-')
plt.plot(blengthb, errorb, 'go-')
plt.plot(blengthc, errorc, 'bo-')
plt.xlabel('Block length')
plt.ylabel('Standard deviation, $ \sigma$ ')
#plt.show()
plt.savefig('comp.png', format='png')
