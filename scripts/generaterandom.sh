#!/bin/bash
# Generate a random number between $FLOOR and $RANGE
#https://tldp.org/LDP/abs/html/randomvar.html

RANGE=1800
FLOOR=600
number=0   #initialize
while [ "$number" -le $FLOOR ]
do
  number=$RANDOM
  let "number %= $RANGE"  # Scales $number down within $RANGE.
done
echo "Random number between $FLOOR and $RANGE ---  $number"
echo
