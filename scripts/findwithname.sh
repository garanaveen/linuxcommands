#!/bin/bash
#EXCLUDE_DIR1/2 #Customize this variable to what you want to exclude.
EXCLUDE_DIR1=dist
EXCLUDE_DIR2=none-todo

FIRST_FILE_PATH=$(find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -name "*$1*"  -print -quit)

FULLPATH=$(echo ${PWD}/${FIRST_FILE_PATH} | sed 's:\./::g')
echo ${FULLPATH} | xclip -selection clipboard
echo "\"${FULLPATH}\" copied to clipboard"


find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -name "*$1*"  -print
