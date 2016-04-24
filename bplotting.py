#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt
#import scipy.odr as ODR
#import scipy.optimize as opt

#def fitfunction(p, x):
  #return p[0]*x**3 + p[1]*x**2 + p[2]*x + p[3]

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)
cvTemp, cvfluc, flucerr= np.genfromtxt('fluc.txt', unpack=True)

#model = ODR.Model(fitfunction)

#odr = ODR(temp, u, )
#initial = np.array([0.0, 0.0, 0.0, 0.0])
#print opt.curve_fit(fitfunction, temp, u, initial, uerr)
p = np.polyfit(temp,u,3)
deriv = (3*p[0], 2*p[1], 1*p[2]) 
print deriv
fit= np.polyval(p, temp)
cv= np.polyval(deriv, temp)

plt.plot(temp, u, 'o')
print temp
plt.errorbar(temp, u, yerr=2*uerr, xerr=2*temperr, fmt='o')
plt.savefig('uterrors', format='png')
plt.clf()
#plt.plot(temp, fit)
plt.plot(temp, cv)
plt.plot(cvTemp, cvfluc, 'ro')
#plt.errorbar(cvTemp, cvfluc, yerr=2*np.sqrt(temperr**2 + uerr**2), fmt='o')
plt.errorbar(cvTemp, cvfluc, yerr=flucerr, fmt='o')
#fit = np.polyfit()
d_name = 'cv.png'
plt.savefig(d_name, format='png')
plt.close()
