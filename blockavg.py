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
  return np.std(array)/len(array)

#Standard deviation for each block
def standarddev(data):
  s=0
  count=0
  mean=np.mean(data, dtype=np.float64)
  #Do for number of blocks, array index is from 0 to n-1
  while (count < len(data)):
    s = s + ((data[count] - mean )**2)
    count += 1
  return np.sqrt(s/(len(data)-1.0))/np.sqrt(len(data))

#Read in Production tup file
data=raw_input("enter prod tup name: ")
data_tup = data + '.tup'

#unpack the data from the .tup
time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#Allocate arrays
b_length = []
std_dev = []
u_err = []

#initial
numberofblocks=u.size
std_d = std_deviation(u)

#Calculating without Block averaging    
b_length.append(1)
std_dev.append(std_deviation(u))
u_err.append(std_deviation(u))
avg_u = u

i=1
mindiff = 10
while (numberofblocks > 1000):

  #Number of blocks to average over can use integer division
  #to round down to deal with left over elements being ignored 
  numberofblocks=len(avg_u)//2
  b_length.append(2**i)  
  avg_u = blockavg(avg_u, numberofblocks)
  
  #Calculating the standard deviation
  std_dev.append(standarddev(avg_u))
  diff = abs(std_dev[i-1]-std_dev[i])
   ##if smallest gradient save element
  if (diff < mindiff):
     mindiff = diff
     true_stddev = std_dev[i-1]
     
  u_err.append(std_deviation(avg_u))

  i += 1

#To find real value of std_dev search for steps where the difference is minium
#as the gradient will be the smallest value. Then element k-1 is the true std_dev
#mindiff = max(std_dev)
#for (k in range(1,len(std_dev)):
   #diff = abs(std_dev[k-1]-std_dev[k])
   ##if smallest gradient save element
   #if (diff < mindiff):
     #mindiff = diff
     #minelement = k-1
     
#true_std = std_dev[minelement]
print true_stddev
print std_dev

#write block averaged to file
avgdata = 'avg' + data + '.dat'
#np.savetxt(avgdata, (np.mean(u, dtype=np.float64),true_std, delimiter=",", fmt="%15.10f")

#Plotting the data
#plt.plot(b_length, std_dev/std_d, 'ro')
#plt.errorbar(b_length, std_dev/std_d, u_err/std_d)

plt.plot(b_length, std_dev, 'ro')
plt.errorbar(b_length, std_dev, u_err)

d_name = 'std' + data
#plt.plot(time,u)
plt.savefig(d_name, format='png')
#plt.show()

