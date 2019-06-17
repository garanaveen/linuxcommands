#!/bin/bash
if [[ "$#" -ne 2 ]]
then
    SCRIPT_NAME=`basename "$0"`
    echo "Usage : $SCRIPT_NAME MaxDepth FileNamePattern"
    exit
fi

MAXDEPTH=$1
NAME="$2"

find . -maxdepth $MAXDEPTH -name "*$NAME*" -print

