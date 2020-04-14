#!/bin/bash

#TODO : figure out the path for utils from the place where this is run. This source only works if its run from the same directory that this script is in.
source utils.sh

function mkdircd () { mkdir -p "$@" && eval cd "\"\$$#\""; }



export EDITOR="/usr/bin/vim"
export VISUAL="/usr/bin/vim"

set editing-mode vi
set keymap vi-command

set -o vi

bind -x '"\C-l": clear'

function countdown(){
   date1=$((`date +%s` + $1)); 
   while [ "$date1" -ge `date +%s` ]; do 
     echo -ne "$(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r";
     sleep 0.1
   done
}

function stopwatch(){
  date1=`date +%s`; 
   while true; do 
    echo -ne "$(date -u --date @$((`date +%s` - $date1)) +%H:%M:%S)\r"; 
    sleep 0.1
   done
}

export HISTSIZE=100000000

weather()
{ 
   curl -s "wttr.in/dsm"
}

#If ack-grep is installed make an alias
which ack-grep > /dev/null
if [ 0 == $? ]; then
   alias ack='ack-grep'
fi

export PATH=$PATH:$HOME/linuxcommands/scripts/


#Use cdd when you want to change to directory of the given filepath. This way you can avoid deleting the file name at the end.
cdd()
{
DIR=`dirname $1`
echo "${DIR}"
cd ${DIR}
}

#export PS1='\h:$PWD\$'
#export PS1='\w\$'

