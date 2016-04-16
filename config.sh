#!/bin/bash
gfortran -o crystal crystal.f90
gfortran -o md3 md3.f90
# echo compiled

n_timestep="10000"
n_ts_equib="10000"
timestep="0.004"
density="0.7"
crystal="initial_coords_256"

temp=1.50
tname=$(echo $temp | awk '{print $1*100}') 

equil="equil_$tname" && prod="prod_$tname"

#rm $crystal
#./crystal << EOF
#1
#1.5496
#4
#4
#4
#0.1
#$crystal
#EOF

#Create Equib file
cat <<EOF >$equil.in
Equilibrate 256 particles, density=$density, T*=$temp
$crystal
$equil.out
$n_ts_equib
$timestep
$density
$temp
.1
EOF

#Setup Equilibrium
time ./md3 <$equil.in >$equil.tup 
echo Equil done

#Create Production file
cat <<EOF >$prod.in
Production run, 256 particles, density=$density, T*=$temp
$equil.out
$prod.out
$n_timestep
$timestep
$density
-1
.1
EOF

#Simulate
time ./md3 <$prod.in >$prod.tup 
echo Prod done