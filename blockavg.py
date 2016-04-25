#!/bin/bash
#to include floating point division by default
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#Halves number of elements in the array
def blockavg(quantity, nb):
  blocked_quan=[]
  for i in range(0,(nb-1)):
    blocked_quan.append((quantity[i]+quantity[i+1])/2.0)
  return blocked_quan

#Quick standard deviation with numpy
def std_deviation(array):
  return np.std(array)/np.sqrt(len(array))

#Standard deviation for each block
def standarddev(array):
  s=0
  count=0
  mean=np.mean(array, dtype=np.float64)
  #Do for number of blocks, array index is from 0 to n-1
  while (count < len(array)):
    s = s + ((array[count] - mean )**2)
    count += 1
  return np.sqrt(s/(len(array)-1.0))/np.sqrt(len(array))

def findstd(datain, name):
  #Allocate arrays
  b_length = []
  std_dev = []
  err = []

  #initial
  numberofblocks=len(datain)
  std_d = std_deviation(datain)

  #Calculating without Block averaging    
  b_length.append(1)
  std_dev.append(std_deviation(datain))
  err.append(std_deviation(datain))
  avg_data = datain

  i=1
  mindiff = 10
  while (numberofblocks > 500):

    #Number of blocks to average over can use integer division
    #to round down to deal with left over elements being ignored 
    numberofblocks=len(avg_data)//2
    b_length.append(2**i)  
    avg_data = blockavg(avg_data, numberofblocks)
  
    #Calculating the standard deviation
    std_dev.append(standarddev(avg_data))
  
    #To find real value of std_dev search for steps where the difference is minium
    #as the gradient will be the smallest value. Then element k-1 is the true std_dev
    diff = abs((std_dev[i]-std_dev[i-1])/(b_length[i] - b_length[i-1]))
  
    ##if smallest gradient save element
    if (diff < mindiff):
      mindiff = diff
      true_stddev = std_dev[i-1]
      element = i-1
     
    err.append(std_deviation(avg_data))
    i += 1
    
  plt.plot(b_length, std_dev, 'ro')
  plt.errorbar(b_length, std_dev, err)

  d_name = 'std'+ name + data
  #plt.plot(time,u)
  plt.savefig(d_name, format='png')
  plt.close()
  #plt.show()
  #print 'With a block length of ',b_length[element]
  #print 'Standard deviation =', true_stddev
  return true_stddev
################################## End Of Functions ##############################  
  
#Read in Production tup file
data=raw_input()
data_tup = data + '.tup'

#unpack the data from the .tup
time, t, k, u, pot, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

ustd = findstd(u, 'internale')
tempstd = findstd(t, 'Temperature')
print np.mean(t, dtype=np.float64), tempstd, np.mean(u, dtype=np.float64), ustd

#write block averaged to file
avgdata = 'avg' + data + '.dat'
#np.savetxt(avgdata, (np.mean(u, dtype=np.float64),true_std, delimiter=",", fmt="%15.10f")

#Plotting the data
#plt.plot(b_length, std_dev/std_d, 'ro')
#plt.errorbar(b_length, std_dev/std_d, u_err/std_d)



