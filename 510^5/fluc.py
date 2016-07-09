#!/bin/bash
#to include floating point division by default
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#calculating delta in fluctuation formula
def form(array):
  meanofsq=0
  #array indexing is 0 to max-1
  for i in range(0, len(array)-1):
    meanofsq = meanofsq + array[i]**2
  meanofsq = meanofsq/len(array)
  return (meanofsq - np.mean(array, dtype=np.float64)**2)

#get file name and properties from shell script, block.sh
data=raw_input()
data_tup = data + '.tup'
initialT=float(raw_input())
#number of particles, 256 was used here
N=int(raw_input())

#read in data from .tup file
time, t, k, u, pot, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

#calculate using fluctuation formula
c_v = 1.5*1/(1 - (2/(3*N*(np.mean(t))**2))*(form(1.5*N*t)))

#remove ideal gas contribution, C_v-1.5
print initialT, c_v-1.5, (np.std(t))
