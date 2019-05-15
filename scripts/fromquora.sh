#!/bin/bash
#Downloads the answer given the link for the quora.
QUORA_LINK=$1
TMP_FILE=${HOME}/tmp/q.html
wget ${QUORA_LINK} -O ${TMP_FILE}
#tidy -mi -html -wrap 0 -q ${TMP_FILE}
#grep -f ~/linuxcommands/scripts/quorasearchpattern.txt ${TMP_FILE} | sed -e 's/<[^>]*>//g' | sed -e 's/&#\d*//g' | sed -e 's/^ *//' > ~/tmp/a


#cat ${TMP_FILE} | html2text -o q.txt 
cat ${TMP_FILE} | html2text | sed -e 's/<[^>]*>//g' | sed -e 's/&#\d*//g' | sed -e 's/^ *//' > ~/tmp/a
iconv -c -f utf-8 -t ascii ~/tmp/a | less


