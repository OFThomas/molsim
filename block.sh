#!/bin/bash

for file in prod*.tup
do 
name=${file::-4}
python blockavg.py << EOF > temp.txt
$name
EOF
echo $name
done 
echo""