THIRDPARTY_TOOLS_DIR=${HOME}/thirdpartytools
GTEST_SOURCE_DIR=${THIRDPARTY_TOOLS_DIR}/googletest
GTEST_BUILD_DIR=${GTEST_SOURCE_DIR}/build


mkdir ${THIRDPARTY_TOOLS_DIR}

git clone git@github.com:google/googletest.git  ${GTEST_SOURCE_DIR}

mkdir ${GTEST_BUILD_DIR}
cd ${GTEST_BUILD_DIR}
cmake -G"Unix Makefiles" ..
make


