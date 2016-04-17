#!/bin/bash
import numpy as np
import matplotlib.pyplot as plt
import os

#os.chdir(r'C:\Users\Oliver\Desktop')

def blockavg(quantity, bn):
  avg_quan = np.mean(quantity.reshape(-1, intervals), 1, dtype=np.float64)
  return avg_quan

def std_deviation(array):
  array_sq = np.square(array)
  sumofsq = np.sum(array_sq, dtype=np.float64)
  
  array_sum = np.sum(array, dtype=np.float64)
  sqofsum = np.square(array_sum)
  
  return np.sqrt(sumofsq - sqofsum)

data=raw_input("enter prod tup name: ")
data_tup = data + '.tup'

time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#Number of elements to average over
#print time.size
b_length = np.array([])
i=0
do while (b_length <= time.size):

  intervals=(time.size/b_length[i])
  
  ##Block averaging##
  #avg_time = blockavg(time, intervals)
  avg_u = blockavg(u, intervals)
  
  std_dev[i]=std_deviation(avg_u)
  i += 1
  b_length[i] = i*(time.size/5.0)
  
  #print 'Averaged data', avg_time, avg_u
  avgdata = 'b_avg_' + data + '.dat'
  
  #write block averaged to file
  #np.savetxt(avgdata, (avg_time, avg_u), delimiter=" ", fmt="%15.10f")

plt.plot() 

plt.plot(time,u)
plt.savefig(data, format='png')
#plt.show()

