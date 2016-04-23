#!/bin/bash
#to include floating point division by default
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def form(array):
  meanofsq=0
  for i in range(0, len(array)-1):
    meanofsq = meanofsq + array[i]**2
  meanofsq = meanofsq/len(array)
  return (meanofsq - np.mean(array, dtype=np.float64)**2)

data=raw_input()
data_tup = data + '.tup'
initialT=float(raw_input())
N=int(raw_input())

time, t, k, u, pot, p = np.genfromtxt(data_tup, usecols=[0,1,2,3,4,5], unpack=True)

c_v = 1.5*1/(1 - (2/(3*N*initialT**2))*(form(1.5*N*t)))
print initialT, c_v-1.5
