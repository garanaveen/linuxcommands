#!/bin/bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    *)          machine=Linux #Default to Linux
esac
echo ${machine}


#Default in Linux
BASHRCFILE=$HOME/.bashrc

if [ "${machine}" == "Mac" ]
then
   BASHRCFILE=$HOME/.bash_profile
fi

echo "BASHRCFILE : ${BASHRCFILE}"

echo "" >> ${BASHRCFILE}
echo "if [ -f ~/linuxcommands/my_bashrc ]; then" >> ${BASHRCFILE}
echo "    source ~/linuxcommands/my_bashrc" >> ${BASHRCFILE}
echo "fi" >> ${BASHRCFILE}

echo "" >> ${BASHRCFILE}
echo "if [ -f ~/linuxcommands/my_aliases ]; then" >> ${BASHRCFILE}
echo "    source ~/linuxcommands/my_aliases" >> ${BASHRCFILE}
echo "fi" >> ${BASHRCFILE}

