#!/bin/bash
#Similar file : vimfindfirstoccurance.sh

#EXCLUDE_DIR1/2 #Customize this variable to what you want to exclude.
EXCLUDE_DIR1=dist
EXCLUDE_DIR2=Dir2-ReplaceThisAsPerYourNeeds
FILEPATH=`find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -name "*$1*" \
-print -quit`
echo "FILEPATH : ${FILEPATH}"

DIRNAME="$( cd "$( dirname "${FILEPATH}" )" >/dev/null 2>&1 && pwd )"

echo "DIRNAME : ${DIRNAME}"

cd ${DIRNAME} #This will work only if you source this script (like 'source cddfindfirstoccurance.sh' instead of './cddfindfirstoccurance.sh')


