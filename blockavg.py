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
  meanofsq = np.mean(array_sq, dtype=np.float64)
  
  array_mean = np.mean(array, dtype=np.float64)
  sqofmean = np.square(array_mean)
  
  return np.sqrt(meanofsq - sqofmean)

#data=raw_input("enter prod tup name: ")
data='prod_100'
data_tup = data + '.tup'

time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#number of block lengths to try
n_block = 100
#Allocate arrays
b_length = np.zeros(n_block)
std_dev = np.zeros(n_block)

#set initial block length to 1, no block averaging
#b_length[0] = 1
#set to average over whole array
#intervals = time.size
#std_dev[0] = std_deviation(u)

i=0
while (i < n_block):
  
  if (i>0):
    #Calc next block length
    b_length[i] = (i*4.0)
  else:
    b_length[i] = 1
    intervals = 1.0
    std_dev[i] = std_deviation(u)
  
  #Number of blocks to average over
  intervals=(time.size/b_length[i])
  
  ##Block averaging##
  avg_u = blockavg(u, intervals)
 
 #calc std deviation for block length
  std_dev[i]=std_deviation(avg_u)
  
  i += 1
  
  #print 'Averaged data', avg_time, avg_u
  avgdata = 'b_avg_' + data + '.dat'
  
  #write block averaged to file
  #np.savetxt(avgdata, (avg_time, avg_u), delimiter=" ", fmt="%15.10f")
print b_length, std_dev
plt.plot(b_length, std_dev) 

#plt.plot(time,u)
#plt.savefig(data, format='png')
plt.show()

