#!/bin/bash
import numpy as np
import matplotlib.pyplot as plt
import os

#os.chdir(r'C:\Users\Oliver\Desktop')

def blockavg(quantity, bn):
  avg_quan = np.mean(quantity.reshape(-1, intervals), 1, dtype=np.float64)
  return avg_quan

data=raw_input("enter prod tup name: ")
data_tup = data + '.tup'

time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#Number of elements to average over
print time.size
intervals=(time.size/100.0)

##Block averaging##
avg_time = blockavg(time, intervals)
avg_u = blockavg(u, intervals)
print 
#print 'Averaged data', avg_time, avg_u
avgdata = 'b_avg_' + data + '.dat'
#write block averaged to file
np.savetxt(avgdata, (avg_time, avg_u), delimiter=" ", fmt="%15.10f")

plt.plot(time,u)
plt.savefig(data, format='png')
#plt.show()

