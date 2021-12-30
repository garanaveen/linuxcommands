#!/bin/bash

#TODO : figure out the path for utils from the place where this is run. This source only works if its run from the same directory that this script is in.
#source utils.sh

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


#https://stackoverflow.com/questions/24283097/reusing-output-from-last-command-in-bash
# capture the output of a command so it can be retrieved with ret
#cap () { tee /tmp/capture.out}

# return the output of the most recent command that was captured by cap
#ret () { cat /tmp/capture.out }

#https://medium.com/tech-epic/how-to-use-pbcopy-on-ubuntu-f12940e5e18c
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

#To cd in to a director, ccd() lets you use the partial name of the directory name. If there are multiple matches, first match is taken.
function ccd()
{
   DirectoryPartialName=${1}
   DIR_NAME=`find . -maxdepth 1 -type d -name "*${DirectoryPartialName}*" -print -quit`
   if [ ! -z "$DIR_NAME" ]; then
       echo "cd ${DIR_NAME}"
       cd ${DIR_NAME}
   fi
}

