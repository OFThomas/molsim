#!/bin/bash 

import numpy as np
import matplotlib.pyplot as plt

temp, temperr, u, uerr = np.genfromtxt('temp.txt', unpack=True)
cvTemp, cvfluc, flucerr= np.genfromtxt('fluc.txt', unpack=True)

#Calculate best fit cubic to u v T
p = np.polyfit(temp,u,3)
#differentiate to obtain C_v
deriv = (3*p[0], 2*p[1], 1*p[2]) 
print deriv

fit= np.polyval(p, temp)
#ise derivative to calculate c_v
cv= np.polyval(deriv, temp)

#print u v T with +/- 2 std dev error bars from block averaging
plt.plot(temp, u, 'ro', temp, np.polyval(p, temp), 'r-')
plt.errorbar(temp, u, yerr=2*uerr, xerr=2*temperr, fmt='go')

plt.xlabel('Temperature, T*')
plt.ylabel('Internal configuration energy, U* ')

#Write this out 
print temp
plt.savefig('uterrors.png', format='png')
plt.clf()

#plot C_v against using the gradient method
plt.plot(temp, cv)

#Use fluctuation data to plot c_v v T
plt.plot(cvTemp, cvfluc, 'ro')
plt.errorbar(cvTemp, cvfluc, yerr=flucerr, fmt='o')

plt.xlabel('Temperature, T*')
plt.ylabel('Specific heat capacity, C_v ')

#save end graph with both plots as cv.png
d_name = 'cv.png'
plt.savefig(d_name, format='png')
plt.close()
