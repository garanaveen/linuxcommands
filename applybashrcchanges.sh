#!/bin/bash

source utils.sh

BASHRCFILE=${HOME}/.bashrc
PLATFORM_SPECIFIC_ALIASES=linux_aliases

setmachinetype

if [ "${MACHINETYPE}" == "Mac" ]
then
    BASHRCFILE=${HOME}/.bash_profile
    PLATFORM_SPECIFIC_ALIASES=mac_aliases
fi


echo "Updating ${BASHRCFILE} file to contain custom bashrc and aliases"

#TODO : Replace this cat with echo statements like PLATFORM_SPECIFIC_ALIASES.
cat  bashrcchanges.txt >> ${BASHRCFILE}

echo "" >> ${BASHRCFILE}
echo "if [ -f ~/linuxcommands/${PLATFORM_SPECIFIC_ALIASES} ]; then" >> ${BASHRCFILE}
echo "    source ~/linuxcommands/${PLATFORM_SPECIFIC_ALIASES}" >> ${BASHRCFILE}
echo "fi" >> ${BASHRCFILE}
echo "" >> ${BASHRCFILE}

