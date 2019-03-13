find .  \
-name jdx -type d -prune \
-o -name \*.cpp \
-o -name \*.h \
| grep -v "_Tests" \
| grep -v "_AcceptanceTests" \
| grep -v "gmock" \
| grep -v "Test.cpp" \
| grep -v "Mock.cpp" \
| grep -v "Mock.h" \
| awk '{print "\""$0"\""}' \
> cscope.files


#cscope -b -q -k

