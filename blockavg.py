#!/bin/bash
import numpy as np
import os

#os.chdir(r'C:\Users\Oliver\Desktop')
#print os.getcwd()



#data = 'prod_170.tup'

time, u = np.genfromtxt(data, usecols=[0,4], unpack=True)

print 'Input data', time, u

#Number of elements to average over
intervals=10000

##Block averaging##
avg_time = blockavg(time, intervals)
avg_u = blockavg(u, intervals)

print 'Averaged data', avg_time, avg_u

#write block averaged to file
np.savetxt('avgdata.dat', (avg_time, avg_u), delimiter=" ", fmt="%15.10f")
