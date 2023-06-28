#!/bin/bash

if [ "$#" -lt 2 ]
  then echo "gitgrepallrevs.sh <search-pattern> <file-path>"
  exit
fi

SEARCH_PATTERN=$1
FILENAME=$2
git rev-list --all ${FILENAME} | (
    while read revision; do
        git grep ${SEARCH_PATTERN} $revision ${FILENAME}
    done
)
