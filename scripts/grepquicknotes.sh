#!/bin/bash

if ! command -v ack &> /dev/null
then
   echo "ack command needs to be installed"
   echo "sudo apt-get install ack-grep"
   exit
fi

SEARCH_PATTERN="$1"
GREP_COMMAND="ack"
FOLLOW_LINKS_TOO="-L"
#PRINT_FILE_NAME_OPTION="--no-filename"
PRINT_FILE_NAME_OPTION=""

find ${FOLLOW_LINKS_TOO} ${HOME} -maxdepth 3 -name usefulcommands.txt -print |xargs grep ${PRINT_FILE_NAME_OPTION} ${SEARCH_PATTERN} --context=2
echo "----Results in all usefulcommands.txt"
echo "Press enter key to continue searching........."

read
${GREP_COMMAND} $1 ${HOME}/n/ -r --context=3 -i
echo "----Results from rn"

#-------------------------------------

read
${GREP_COMMAND} $1 ${HOME}/linuxcommands/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
${GREP_COMMAND} $1 ${HOME}/myreference/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
${GREP_COMMAND} $1 ${HOME}/personal/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
echo "----Results in linuxcommands and myreferences"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/github/garanaveen/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
echo "----Results from github/garanaveen"


