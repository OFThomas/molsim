#!/bin/bash
#rm ./temp.txt

if [ -s temp.txt ]; then
  for file in prod*.tup
  do 
  name=${file::-4}
  python blockavg.py << EOF >> temp.txt
  $name
EOF
  echo $name

 # initialT=${name:5}
 # initialT=$(echo $initialT | awk '{print $1/100}') 
 # echo $initialT
  done 
fi 
  echo""
  python bplotting.py &