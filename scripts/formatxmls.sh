#!/bin/sh
#This script will format the xml specified.
#Note: the original file is replaced with the formatted versin.

if [ $# -lt 1 ]; then
echo "Usage : ./formatxmls.sh XMLFilePath"
exit
fi

for i in $*; do
cp $i $i.bKP
/usr/bin/xmllint  --format $i &> $i.tMpP a;  mv $i.tMpP $i
echo "$i is formatted."
done

