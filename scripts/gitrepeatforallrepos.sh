#!/bin/bash

#These are scripts that are supposed to execute git commands on all the repos in the current directory (not recursive).

#Check if there are any incoming messages from remote,
#find . -maxdepth 2  -mindepth 1 -name .git -type d -exec sh -c 'cd $0 ; cd ../ ; pwd ; git log master..origin/master; cd ..' {} \;

#git pull
#find . -maxdepth 2  -mindepth 1 -name .git -type d -exec sh -c 'cd $0 ; cd ../ ; pwd ; git pull ; cd ..' {} \;

#This command generates the list of git clone commands for all the repos in the current directory. Helpful in deleting all the repos and recloning them.
#find . -maxdepth 2  -mindepth 1 -name .git -type d -exec sh -c 'git --git-dir="$0" remote -v' {} \; 2>1 |grep push | sed 's/origin/git clone/' |sed 's/ (push)//'


