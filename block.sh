#!/bin/bash

for file in prod*.tup
do 
name=${file::-4}
python blockavg.py << EOF
$name
EOF
echo $name
done 
echo""