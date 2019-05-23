#!/bin/bash

#This script is supposed to do "git pull" on all the repos in the current directory.
#find . -maxdepth 2  -mindepth 1 -name .git -type d -exec sh -c 'git --git-dir="$0" pull' {} \;

#This command generates the gitpull for all the repos in the current directory. Helpful in deleting all the repos and recloning them.
#find . -maxdepth 2  -mindepth 1 -name .git -type d -exec sh -c 'git --git-dir="$0" remote -v' {} \; 2>1 |grep push | sed 's/origin/git clone/' |sed 's/ (push)//'


