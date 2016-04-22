#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt
import scipy.odr as ODR
import scipy.optimize as opt

def fitfunction(p, x):
  return p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3]

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)

#model = ODR.Model(fitfunction)

#odr = ODR(temp, u, )
initial = np.array([0.0, 0.0, 0.0, 0.0])
print opt.curve_fit(fitfunction, temp, u, initial, uerr)

plt.plot(temp, u, 'o')
plt.errorbar(temp, u, yerr=uerr, xerr=temperr, fmt='o')
fit = np.polyfit()
plt.show()
