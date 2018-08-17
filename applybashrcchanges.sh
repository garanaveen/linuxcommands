#!/bin/bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    *)          machine=Linux #Default to Linux
esac
echo "This is \"${machine}\" os"


#Default in Linux
BASHRCFILE=${HOME}/.bashrc

if [ "${machine}" == "Mac" ]
then
   BASHRCFILE=${HOME}/.bash_profile
fi

echo "Updating ${BASHRCFILE} file to contain custom bashrc and aliases"

cat  bashrcchanges.txt >> ${BASHRCFILE}
