#!/bin/bash
# @todo : The copying of clipboard doesn't work on mac.
echo $PWD/$1 | sed 's:\./::g' | pbcopy
echo $PWD/$1 | sed 's:\./::g'
echo "cp $PWD/$1 ./"

