#!/bin/bash

#to remove all ipcs, if there any.

list=$(ipcs -q | grep "$USER" | cut -d' ' -f2)
for queue in $list
do
ipcrm -q $queue > /dev/null
done

list=$(ipcs -m | grep "$USER" | cut -d' ' -f2)
for shm in $list
do
ipcrm -m $shm > /dev/null
done

list=$(ipcs -s | grep "$USER" | cut -d' ' -f2)
for sem in $list
do
ipcrm -s $sem > /dev/null
done

