#!/bin/bash

THIS_DIR="$( dirname "${BASH_SOURCE[0]}" )"
echo "THIS_DIR : $THIS_DIR"

export LINUXCOMMANDS_ROOT=$PWD/
echo "LINUXCOMMANDS_ROOT : $LINUXCOMMANDS_ROOT"


# -h is test if file exists and is a link.
if [ ! -h "$HOME/linuxcommands" ]; then
    ln -sv $PWD $HOME/linuxcommands
fi

cat $HOME/linuxcommands/vimrc >> $HOME/.vimrc 



# Git config
git config --local user.email "garanaveen@gmail.com"
git config --local user.name "garanaveen"


cat ackrc | tail -n +3 >> $HOME/.ackrc

