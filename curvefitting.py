#!/bin/bash
import numpy as np
import matplotlib.pyplot as plt
import os

#os.chdir(r'C:\Users\Oliver\Desktop')
#print os.getcwd()
data = 'prod_170.tup'
quantity=1

time, t, k, pot, u, p = np.genfromtxt(data, usecols=[0,1,2,3,4,5], unpack=True)

plt.plot(time,u)
plt.show()

