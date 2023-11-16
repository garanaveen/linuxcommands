#!/bin/bash

eval "$(ssh-agent -s)"

KEYS=`ls $HOME/.ssh/id_ed25519-* | grep -v pub`

for key in "${KEYS[@]}"
do
   echo "key : $key"
   ssh-add $key
done


