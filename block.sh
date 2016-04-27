#!/bin/bash
if ! [ -s temp.txt ] || ! [ -s fluc.txt ] ; then
rm ./temp.txt
rm ./fluc.txt
for file in prod*.tup
do 
name=${file::-4}
python blockavg.py << EOF >> temp$name.txt
$name
EOF
echo $name

initialT=${name:5}
initialT=$(echo $initialT | awk '{print $1/100}') 
python fluc.py << EOF >> fluc.txt
$name
$initialT
256
EOF
done 
fi 

echo""

python bplotting.py 
display 'cv.png'
