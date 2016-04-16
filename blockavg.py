#!/bin/bash
import numpy as np
import os

os.chdir(r'C:\Users\Oliver\Desktop')
#print os.getcwd()

#data_array = np.genfromtxt('data.txt', delimiter=',')
#data_array = np.loadtxt('data.txt', delimiter=',', usecols=[0])
data_array = np.genfromtxt('data.txt')

print 'Input data', data_array

#Number of elements to average over
intervals=2

##Block averaging##
avgdata = np.mean(data_array.reshape(-1, intervals), 1)

print 'Averaged data', avgdata

#write block averaged to file
np.savetxt('avgdata.dat', avgdata, delimiter=" ", fmt="%15.10f")
