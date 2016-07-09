#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt
#import scipy.odr as ODR
#import scipy.optimize as opt

#def fitfunction(p, x):
  #return p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3]

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)

#model = ODR.Model(fitfunction)

#odr = ODR(temp, u, )
#initial = np.array([0.0, 0.0, 0.0, 0.0])
#print opt.curve_fit(fitfunction, temp, u, initial, uerr)
p = np.polyfit(temp,u,3)
print p
deriv = (3*p[0], 2*p[1], 1*p[2]) 
fit= np.polyval(p, temp)
cv= np.polyval(deriv, temp)

plt.plot(temp, u, 'o')
plt.errorbar(temp, u, yerr=2*uerr, xerr=2*temperr, fmt='o')
plt.plot(temp, fit)
#plt.plot(temp, cv)
#fit = np.polyfit()
plt.show()
