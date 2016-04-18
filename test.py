#!/bin/bash

def blockavg(quantity, blocklen, no_ofblocks):
  blocked_quan = quantity.reshape(no_ofblocks, blocklen)
  return blocked_quan

def standarddev(data, blen, nb, mean):
  b_avg=blockavg(data, blen, nb)
  #print b_avg
  s=0
  count=0
  while (count < nb):
    #print i
    s = s + ((np.mean(b_avg[count]) - mean)**2)/nb

    count += 1
  #print s
  return s

