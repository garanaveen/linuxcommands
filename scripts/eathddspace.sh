#!/bin/sh
#Usage : ./eathddspace.sh 4

#Give the number of GBs that needs to annihilated as first argument.
#If no argument is given 1GB file is created.
#If you want to annihilate MB instead of GB then replace bs=1G with bs=1M in dd command in the following script

#TODO : Using fallocate is probably much faster

nGB=1
if [ $# -eq 1 ]; then
nGB=$1
fi
echo "nGB = $nGB"
for ((n=1; n<=nGB; n++))
do
echo  "$n "
dd if=/dev/zero of=junK.tXt bs=1G count=1 ;
TIME=`date +%HH_%MM_%SS_%NN`
mv junK.tXt "$TIME"
echo "File $TIME created..."
done                           # A construct borrowed from 'ksh93'.

echo; echo
