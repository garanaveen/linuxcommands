#!/bin/bash
echo $PWD/$1 | sed 's:\./::g' | pbcopy
echo $PWD/$1 | sed 's:\./::g'
echo "cp $PWD/$1 ./"

