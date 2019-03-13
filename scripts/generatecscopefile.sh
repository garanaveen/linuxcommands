find .  \
-name jdx -type d -prune \
-o -name \*.cpp -exec echo \"{}\" \; \
-o -name \*.h -exec echo \"{}\" \; \
> cscope.files


cscope -b -q -k

