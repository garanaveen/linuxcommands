#!/bin/bash

#Currently doesn't work for articles which have images in them. Need to figure out a way to deal with it!

QUORA_LINK=$1
wget -O ~/tmp/tmpfile.html ${QUORA_LINK}
#tidy -i -w -ashtml ~/tmp/tmpfile.html 2> /dev/null | grep class.*ui_qtext_para | awk '{gsub("<[^>]*>", "")}1' |sed -e 's/^[ \t]*//' |fold -w 80 -s
tidy -i -w ~/tmp/tmpfile.html 2> /dev/null | grep class.*ui_qtext_para | awk '{gsub("<[^>]*>", "")}1' |sed -e 's/^[ \t]*//' |fold -w 80 -s > ~/tmp/a &

