#!/bin/bash

GREP_COMMAND="grep"

#-------------------------------------
if [ -x "$(command -v ack)" ]; then
   GREP_COMMAND="ack"
fi

DONT_PRINT_FILENAME="-h"
CONTEXT_OF_TWO_LINES="-C2"

FOLLOW_LINKS_TOO="-L"

find ${FOLLOW_LINKS_TOO} ${HOME} -maxdepth 3 -name usefulcommands.txt -print |xargs grep ${DONT_PRINT_FILENAME} "$1" ${CONTEXT_OF_TWO_LINES}

#-------------------------------------

${GREP_COMMAND} $1 ${HOME}/linuxcommands/ -r -C3 -i --no-filename
${GREP_COMMAND} $1 ${HOME}/myreference/ -r -C3 -i --no-filename
${GREP_COMMAND} $1 ${HOME}/personal/ -r -C3 -i --no-filename
echo "----Results in linuxcommands and myreferences"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/ds/ -r -C3 -i --no-filename
${GREP_COMMAND} $1 ${HOME}/dl/ -r -C3 -i --no-filename
echo "----Results from ds and dl"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/github/garanaveen/ -r -C3 -i --no-filename
echo "----Results from github/garanaveen"

echo "Press enter key to continue searching........."
read
${GREP_COMMAND} $1 ${HOME}/jdw/ -r -C3 -i
echo "----Results from jdw"

