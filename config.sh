#!/bin/bash

gfortran -o crystal crystal.f90
gfortran -o md3 md3.f90
echo compiled

crystal="initial_coords_256"
equil="equil_170"
prod="prod_170"
rm $crystal && $equil.in && $prod.in

./crystal << EOF
1
1.5496
4
4
4
0.1
$crystal
EOF

cat <<EOF >$equil.in
Equilibrate 256 particles, density=0.7, T*=1.7
$crystal
$equil.out
10000
0.0032
0.7
1.7
.1
EOF

time ./md3 <$equil.in >$equil.tup 
echo Equil done

cat <<EOF >$prod.in
Production run, 256 particles, density=0.7, T*=1.7
$equil.out
$prod.out
10000
0.0032
0.7
-1
.1
EOF

time ./md3 <$prod.in >$prod.tup 
echo Prod done