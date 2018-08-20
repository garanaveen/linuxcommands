#!/bin/bash

function setbashrcfile()
{
   unameOut="$(uname -s)"
   case "${unameOut}" in
       Linux*)     machine=Linux;;
       Darwin*)    machine=Mac;;
       *)          machine=Linux #Default to Linux
   esac
   echo "This is \"${machine}\" os"


   if [ "${machine}" == "Mac" ]
   then
      BASHRCFILE=${HOME}/.bash_profile
   fi
}

#Default in Linux
BASHRCFILE=${HOME}/.bashrc

setbashrc

echo "Updating ${BASHRCFILE} file to contain custom bashrc and aliases"

cat  bashrcchanges.txt >> ${BASHRCFILE}

