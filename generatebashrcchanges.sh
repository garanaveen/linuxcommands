#!/bin/bash

#Usage,
#Linux,
#./generatebashrcchanges.sh >> ${HOME}/.bashrc
#Mac,
#./generatebashrcchanges.sh >> ${HOME}/.bash_profile

#Default in Linux
MACHINETYPE=Linux
BASHRCFILE=${HOME}/.bashrc
PLATFORM_SPECIFIC_ALIASES=linux_aliases
CURRENT_DIR=${PWD}
#echo "CURRENT_DIR : ${CURRENT_DIR}"

function setmachinetype()
{
   unameOut="$(uname -s)"
   case "${unameOut}" in
       Linux*)     MACHINETYPE=Linux;;
       Darwin*)    MACHINETYPE=Mac;;
       *)          MACHINETYPE=Linux #Default to Linux
   esac
   #echo "This is \"${MACHINETYPE}\" os"

}

setmachinetype

if [ "${MACHINETYPE}" == "Mac" ]
then
    BASHRCFILE=${HOME}/.bash_profile
    PLATFORM_SPECIFIC_ALIASES=mac_aliases
fi

BASHRCFILE=${HOME}/.dummyfile.txt

#echo "Updating ${BASHRCFILE} file to contain custom bashrc and aliases"

declare -a FILE_LIST=(
                      ${CURRENT_DIR}/${PLATFORM_SPECIFIC_ALIASES} 
                      ${CURRENT_DIR}/my_bashrc 
                      ${CURRENT_DIR}/my_aliases
                      ${CURRENT_DIR}/git_aliases
                     )
echo "#Start===================="
for i in "${FILE_LIST[@]}"
do
  echo "if [ -f ${i} ]; then"
  echo "    source ${i}"
  echo "fi"
  echo "#--------------------"
done
echo "#End======================"

