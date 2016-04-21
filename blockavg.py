#!/bin/bash
import numpy as np
import matplotlib.pyplot as plt
#to include floating point division by default
from __future__ import division

#os.chdir(r'C:\Users\Oliver\Desktop')

def blockavg(quantity, blocklen):
  #blocked_quan = np.mean(quantity.reshape(-1, blocklen), 1, dtype=np.float64)
  
  
  for i in range(0,len(nb-1)):
    blocked_quan[i]=(quantity[i]+quantity[i+1])/2.0


  return blocked_quan

def std_deviation(array):
  
  array_sq = np.square(array)
  #print 'array sq', array_sq
  #avg_block = blockavg(u, n_blocks)
  meanofsq = np.mean(array_sq, dtype=np.float64)
  #print 'mean of sq', meanofsq
  
  
  array_mean = np.mean(array, dtype=np.float64)
  #print 'mean', array_mean
  sqofmean = np.square(array_mean)
  #print 'sqofmean', sqofmean
      
  #print 'stdev =', meanofsq - sqofmean
  #print
  
  #return (meanofsq - sqofmean)
  return np.var(array)

#Don't know why it is not working this way
def standarddev(data, blen, nb, mean):
  b_avg=blockavg(data, blen)
  #print b_avg
  s=0
  count=0
  while (count < nb):
    #print i
    #print b_avg[0]
    s = s + ((b_avg[count] - mean)**2)
    count += 1
  #print s
  return np.sqrt(s/nb)

data=raw_input("enter prod tup name: ")
#data='prod_100'
data_tup = data + '.tup'

time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#number of block lengths to try
n_block = 200.0
#Allocate arrays
b_length = np.zeros(n_block)
std_dev = np.zeros(n_block)
mean=np.mean(u, dtype=np.float64)
std_d = std_deviation(u)
print std_d

i=0
c=0
while (c < n_block):
  if (i==0):
    b_length[i] = 1
    intervals = 1.0
    std_dev[i] = std_deviation(u)
    print 'i=0'
      
  else:
    #Calc next block length
    while ((time.size % c) != 0  ):
      c += 1
    b_length[i] = c
    
    #b_length[i] = 2**i 
    #print 'b_leng =',b_length[i]
    #print b_length[i]
    #Number of blocks to average over
    numberofblocks=(time.size/b_length[i])
    print 'nb', numberofblocks
    #print intervals
    ##Block averaging##
    avg_u = blockavg(u, numberofblocks)
    #print avg_u
 
    #calc std deviation for block length
    #std_dev[i]=std_deviation(avg_u, numberofblocks)
    std_dev[i] = std_deviation(avg_u)
    
    #std_dev[i] = standarddev(u, b_length[i], numberofblocks, mean)
    
  i += 1
  c += 1
  
#print 'Averaged data', avg_time, avg_u
avgdata = 'b_avg_' + data + '.dat'
  
#write block averaged to file
np.savetxt(avgdata, (b_length[0:i],std_dev[0:i]), delimiter=" ", fmt="%15.10f")

print b_length[0:i], std_dev[0:i]/std_d
plt.plot(b_length[0:i], std_dev[0:i]/std_d, 'ro') 
d_name = 'std' + data
#plt.plot(time,u)
plt.savefig(d_name, format='png')
#plt.show()

