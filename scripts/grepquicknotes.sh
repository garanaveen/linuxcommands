#!/bin/bash

GREP_COMMAND="grep"

#-------------------------------------
if [ -x "$(command -v ack-grep)" ]; then
   GREP_COMMAND="ack-grep"
fi


DONT_PRINT_FILENAME="-h"
CONTEXT_OF_TWO_LINES="-C2"

FOLLOW_LINKS_TOO="-L"

find ${FOLLOW_LINKS_TOO} ${HOME} -maxdepth 3 -name usefulcommands.txt -print |xargs grep ${DONT_PRINT_FILENAME} "$1" ${CONTEXT_OF_TWO_LINES}

#-------------------------------------

echo "Press enter key........."
read

${GREP_COMMAND} $1 ${HOME}/linuxcommands/ -r -C3 -i --no-filename
${GREP_COMMAND} $1 ${HOME}/myreference/ -r -C3 -i --no-filename

echo "Press enter key........."
${GREP_COMMAND} $1 ${HOME}/ds/ -r -C3 -i --no-filename
${GREP_COMMAND} $1 ${HOME}/dl/ -r -C3 -i --no-filename
