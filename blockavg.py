#!/bin/bash
import numpy as np
import matplotlib.pyplot as plt
#to include floating point division by default
from __future__ import division
#os.chdir(r'C:\Users\Oliver\Desktop')

def blockavg(quantity, nb):
  #blocked_quan = np.mean(quantity.reshape(-1, blocklen), 1, dtype=np.float64)
  for i in range(0,len(nb-1)):
    blocked_quan[i]=(quantity[i]+quantity[i+1])/2.0

  return blocked_quan

def std_deviation(array):
  
  array_sq = np.square(array)
  meanofsq = np.mean(array_sq, dtype=np.float64)
  array_mean = np.mean(array, dtype=np.float64)
  sqofmean = np.square(array_mean)

  #return (meanofsq - sqofmean)
  return np.std(array)

#Don't know why it is not working this way
def standarddev(data, blen, nb, mean):
  s=0
  count=0
  while (count < nb):
    s = s + ((data[count] - mean)**2)
    count += 1
  return np.sqrt(s/(nb-1.0))/np.sqrt(nb)

data=raw_input("enter prod tup name: ")
#data='prod_100'
data_tup = data + '.tup'

time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#number of block lengths to try
n_block = 1024.0
#Allocate arrays
b_length = np.zeros(n_block)
std_dev = np.zeros(n_block)

mean=np.mean(u, dtype=np.float64)
std_d = std_deviation(u)
print std_d
avg_u=blockavg(u, u.size)

i=0
c=0
while (numberofblocks <= n_block):
  if (i==0):
    b_length[i] = 1
    intervals = 1.0
    std_dev[i] = std_deviation(u)
    print 'i=0'
      
  else:
    #Number of blocks to average over
    #numberofblocks=(time.size/b_length[i])
    
    #can use integer division to round down to deal with left over elements
    numberofblocks=(u.size)//(2**i)
    
    ##Block averaging##
    if (avg_u.size % numberofblocks != 0):
      numberofblocks -=  1
      #to skip last odd element
    
    print 'nb', numberofblocks
    b_length[i]=2**i
    avg_u = blockavg(avg_u, numberofblocks)
 
    #calc std deviation for block length
    #std_dev[i]=std_deviation(avg_u, numberofblocks)
    #std_dev[i] = std_deviation(avg_u)
    std_dev[i] = standarddev(avg_u, b_length[i], numberofblocks, mean)
    
  i += 1
  c += 1
  
#print 'Averaged data', avg_time, avg_u
avgdata = 'b_avg_' + data + '.dat'
#write block averaged to file
#np.savetxt(avgdata, (b_length[0:i],std_dev[0:i]), delimiter=" ", fmt="%15.10f")

print b_length[0:i], std_dev[0:i]/std_d
plt.plot(b_length[0:i], std_dev[0:i]/std_d, 'ro') 

d_name = 'std' + data
#plt.plot(time,u)
plt.savefig(d_name, format='png')
#plt.show()

