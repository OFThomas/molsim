#!/bin/bash
#to include floating point division by default
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#os.chdir(r'C:\Users\Oliver\Desktop')

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
  #Do for number of blocks
  while (count < len(data)):
    s = s + ((data[count] - mean )**2)
    count += 1
  return np.sqrt(s/(len(data)-1.0))/np.sqrt(len(data))

#Read in Production tup file
data=raw_input("enter prod tup name: ")
data_tup = data + '.tup'

#unpack the data from the .tup
time, t, k, pot, u, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#number of block lengths to try
n_block = 1024.0

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
while (numberofblocks > 6):

  ##Block averaging##
  #Number of blocks to average over can use integer division
  #to round down to deal with left over elements being ignored 
  numberofblocks=len(avg_u)//2
  b_length.append(2**i)  
  avg_u = blockavg(avg_u, numberofblocks)
  
  #Calculating the standard deviation
  std_dev.append(standarddev(avg_u))
  u_err.append(std_deviation(avg_u))

  i += 1
  
#write block averaged to file
avgdata = 'b_avg_' + data + '.dat'
np.savetxt(avgdata, (b_length[0:i],std_dev[0:i]), delimiter=" ", fmt="%15.10f")

#Plotting the data
plt.plot(b_length, std_dev/std_d, 'ro')
plt.errorbar(b_length, std_dev/std_d, u_err/std_d)

d_name = 'std' + data
#plt.plot(time,u)
plt.savefig(d_name, format='png')
#plt.show()

