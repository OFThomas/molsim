#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)
cvTemp, cvfluc, flucerr= np.genfromtxt('fluc.txt', unpack=True)

#Calculate best fit cubic to u v T
p = np.polyfit(temp,u,3)
deriv = (3*p[0], 2*p[1], 1*p[2]) 
print deriv

fit= np.polyval(p, temp)
cv= np.polyval(deriv, temp)

plt.plot(temp, u, 'ro', temp, np.polyval(p, temp), 'r-')
plt.errorbar(temp, u, yerr=2*uerr, xerr=2*temperr, fmt='go')

plt.xlabel('Temperature, T*')
plt.ylabel('Internal configuration energy, U* ')

print temp
plt.savefig('uterrors.png', format='png')
plt.clf()

plt.plot(temp, cv)

plt.plot(cvTemp, cvfluc, 'ro')
plt.errorbar(cvTemp, cvfluc, yerr=flucerr, fmt='o')

plt.xlabel('Temperature, T*')
plt.ylabel('Specific heat capacity, C_v ')

d_name = 'cv.png'
plt.savefig(d_name, format='png')
plt.close()
