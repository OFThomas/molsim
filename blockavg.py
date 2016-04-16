from io import StringIO
import numpy as np
import os

os.chdir(r'C:\Users\Oliver\Desktop')
print os.getcwd()
data_array = np.genfromtxt('data.txt', delimiter=',')
#data_array = np.loadtxt('data.txt', delimiter=',', usecols=[0])

#data_array = open("test.txt", "r")

print data_array
#x=2
#np.mean(data_array.reshape(-1, x), 1)

#np.savetxt('avgdata.dat', dat, delimiter=" ", fmt="%15.10f")
