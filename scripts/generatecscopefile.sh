find .  \
-name jdx -type d -prune \
-o -name \*.cpp -exec echo \"{}\" \; \
-o -name \*.h -exec echo \"{}\" \; \
-o -name CMakeLists.txt -exec echo \"{}\" \; \
> cscope.files


cscope -b -q -k

