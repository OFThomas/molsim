#!/bin/bash
if ! [ -s temp.txt ] || ! [ -s fluc.txt ] ; then
rm ./temp.txt
rm ./fluc.txt

#for all production.tup files
for file in prod*.tup
do 

#remove .tup exstension
name=${file::-4}

#run block averaging and calculating standard deviation.
python blockavg.py << EOF >> temp$name.txt
$name
EOF
echo $name

#get initial T* value from file name, e.g. prod_110 > T*=1.1
initialT=${name:5}
initialT=$(echo $initialT | awk '{print $1/100}') 

#run fluctuation p-rogram, pipe output to fluc.txt
python fluc.py << EOF >> fluc.txt
$name
$initialT
256
EOF
done 
fi 

echo""
#run plotting program to plot temp.dat (gradient for cv)
#and fluctuation function using fluc.txt
python bplotting.py 
display 'cv.png'
