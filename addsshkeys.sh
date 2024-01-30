#!/bin/bash

eval "$(ssh-agent -s)"

KEYS=($HOME/.ssh/id_ed25519-*)

# Exclude entries that end with ".pub"
KEYS=("${KEYS[@]//*\.pub/}")

for key in "${KEYS[@]}"
do
   echo "key : $key"
   ssh-add $key
done


