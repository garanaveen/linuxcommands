#!/bin/bash
#EXCLUDE_DIR1/2 #Customize this variable to what you want to exclude.
#EXCLUDE_DIR1=dist
EXCLUDE_DIR1=none-todo
EXCLUDE_DIR2=none-todo

FIRST_FILE_PATH=$(find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -iname "*$1*"  -print -quit)



find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -iname "*$1*"  -print


if ! [[ -z ${FIRST_FILE_PATH} ]]; then
   FULLPATH=$(echo ${PWD}/${FIRST_FILE_PATH} | sed 's:\./::g')
   # Detect OS and use appropriate clipboard tool
   if [[ "$(uname)" == "Darwin" ]]; then
      echo "${FULLPATH}" | pbcopy
      echo "\"${FULLPATH}\" copied to clipboard (macOS)"
   else
      echo "${FULLPATH}" | xclip -selection clipboard
      echo "\"${FULLPATH}\" copied to clipboard (Linux)"
   fi
fi

