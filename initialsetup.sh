#!/bin/bash

#-h is test if file exists and is a link.
if [ ! -h "$HOME/linuxcommands" ]; then
    ln -sv $PWD $HOME/linuxcommands
fi

export LINUCCOMMANDS_ROOT=$PWD/

#Git config
git config --local user.email "garanaveen@gmail.com"
git config --local user.name "garanaveen"


