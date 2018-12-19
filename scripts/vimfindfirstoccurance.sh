#EXCLUDE_DIR1/2 #Customize this variable to what you want to exclude.
EXCLUDE_DIR1=.jdx
EXCLUDE_DIR2=InvalidDir2
FILEPATH=`find . -type d -name $EXCLUDE_DIR1 -prune  -o -type d -name $EXCLUDE_DIR2 -prune -o -name .hg -prune -o -name .git -prune -o -name "*$1*"  -print -quit`
vim ${FILEPATH}


