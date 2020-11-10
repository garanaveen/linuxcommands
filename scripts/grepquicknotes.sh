#!/bin/bash

SEARCH_PATTERN="$1"
GREP_COMMAND="ack"
FOLLOW_LINKS_TOO="-L"
#PRINT_FILE_NAME_OPTION="--no-filename"
PRINT_FILE_NAME_OPTION=""

find ${FOLLOW_LINKS_TOO} ${HOME} -maxdepth 3 -name usefulcommands.txt -print |xargs grep ${PRINT_FILE_NAME_OPTION} ${SEARCH_PATTERN} --context=2
echo "----Results in all usefulcommands.txt"
read
echo "Press enter key to continue searching........."

#-------------------------------------

${GREP_COMMAND} $1 ${HOME}/linuxcommands/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
${GREP_COMMAND} $1 ${HOME}/myreference/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
${GREP_COMMAND} $1 ${HOME}/personal/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
echo "----Results in linuxcommands and myreferences"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/ds/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
${GREP_COMMAND} $1 ${HOME}/dl/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
echo "----Results from ds and dl"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/github/garanaveen/ -r --context=3 -i ${PRINT_FILE_NAME_OPTION}
echo "----Results from github/garanaveen"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/jdw/ -r --context=3 -i
echo "----Results from jdw"

