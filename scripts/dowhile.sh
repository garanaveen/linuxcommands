#!/bin/sh

echo "Printing"
while [ $# -eq 0 ]
do
ps -aux |grep def
sleep 1
done

