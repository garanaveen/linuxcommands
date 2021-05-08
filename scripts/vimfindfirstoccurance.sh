#Similar file : cdfindfirstoccurance.sh

EXCLUDE_DIR1=dist
EXCLUDE_DIR2=Dir2-ReplaceThisAsPerYourNeeds
#Add more exclude paths as per your need.

FILEPATH=`find . \
-type d -name $EXCLUDE_DIR1 -prune \
-o -type d -name $EXCLUDE_DIR2 -prune \
-o -name .hg -prune \
-o -name .git -prune \
-o -name "*$1*" \
-print -quit`

echo "FILEPATH : ${FILEPATH}"
vim ${FILEPATH}


