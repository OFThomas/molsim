#!/bin/bash
#rm ./temp.txt

if ! [ -s temp.txt ]; then
  for file in prod*.tup
  do 
  name=${file::-4}
  python blockavg.py << EOF >> temp.txt
  $name
EOF
echo $name
done 
fi 
  echo""
  python plotting.py &