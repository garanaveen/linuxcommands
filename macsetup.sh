#!/bin/bash
MAC_BASHRC=$HOME/.bash_profile

echo "if [ -f $HOME/.bashrc ]; then" >> $HOME/.bash_profile
echo "    source $HOME/.bashrc" >> ${MAC_BASHRC}
echo "fi" >> ${MAC_BASHRC}

