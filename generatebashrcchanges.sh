#!/bin/bash

#Usage,
#Linux,
#./generatebashrcchanges.sh >> ${HOME}/.bashrc
#Mac,
#./generatebashrcchanges.sh >> ${HOME}/.bash_profile

source utils.sh

#Default in Linux
#MACHINETYPE=Linux
CURRENT_DIR=${PWD}
#echo "CURRENT_DIR : ${CURRENT_DIR}"

if [ "${MACHINETYPE}" == "Mac" ]
then
	#echo "Mac"
    BASHRCFILE=${HOME}/.bash_profile
    PLATFORM_SPECIFIC_ALIASES=mac_aliases
else
	#echo "Non Mac"
    BASHRCFILE=${HOME}/.bashrc
    PLATFORM_SPECIFIC_ALIASES=linux_aliases
fi

#echo "Updating ${BASHRCFILE} file to contain custom bashrc and aliases"

declare -a FILE_LIST=(
                      ${CURRENT_DIR}/${PLATFORM_SPECIFIC_ALIASES} 
                      ${CURRENT_DIR}/bashrc 
                      ${CURRENT_DIR}/aliases
                      ${CURRENT_DIR}/git_aliases
                     )
echo "#./generatebashrcchanges.sh >> $HOME/.bashrc"
echo "#Start===================="
for i in "${FILE_LIST[@]}"
do
  echo "if [ -f ${i} ]; then"
  echo "    source ${i}"
  echo "fi"
  echo "#--------------------"
done
echo "#End======================"


