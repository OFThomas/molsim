#!/bin/bash
import numpy as np
import os

os.chdir(r'C:\Users\Oliver\Desktop')
#print os.getcwd()

#datatofit = np.genfromtxt('data.txt', delimiter=',')
#datatofit = np.loadtxt('data.txt', delimiter=',', usecols=[0])
datatofit = np.genfromtxt('data.txt')

print 'Input data', datatofit

