#!/bin/bash
FILENAME=$1
git remote -v \
|grep fetch \
|sed 's|com:|com/|' \
|sed 's|origin.*git@github|https://github|' \
|sed 's|origin.*git@gitlab.eng|https://gitlab.eng|' \
|sed 's/.git (fetch)//' \
|sed '/gitlab/s|$|/-/blob/main/|' \
|sed '/github.com/s|$|/blob/master/|' \
> ~/tmp/gll.txt
git ls-tree --full-name --name-only HEAD $FILENAME >> ~/tmp/gll.txt
cat ~/tmp/gll.txt|xargs -n2 -d'\n' | sed 's/ //'

