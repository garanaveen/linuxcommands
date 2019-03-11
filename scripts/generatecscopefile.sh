find . -name \*.h -print -o -name \*.cpp -print > cscope.files
cscope -b -q -k

