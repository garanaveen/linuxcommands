THIRDPARTY_TOOLS_DIR=${HOME}/thirdpartytools
GTEST_SOURCE_DIR=${THIRDPARTY_TOOLS_DIR}/googletest
GTEST_BUILD_DIR=${GTEST_SOURCE_DIR}/build


mkdir ${THIRDPARTY_TOOLS_DIR}

git clone git@github.com:google/googletest.git  ${GTEST_SOURCE_DIR}

mkdir ${GTEST_BUILD_DIR}
cd ${GTEST_BUILD_DIR}
#export PATH=$PATH:${THIRDPARTY_TOOLS_DIR}
cmake -G"Unix Makefiles" ..
make


#-------------------
#https://gist.github.com/Cartexius/4c437c084d6e388288201aadf9c8cdd5
sudo apt-get install libgtest-dev

sudo apt-get install cmake # install cmake

cd /usr/src/gtest

sudo cmake CMakeLists.txt

sudo make

sudo cp *.a /usr/lib

sudo ln -s /usr/lib/libgtest.a /usr/local/lib/gtest/libgtest.a

sudo ln -s /usr/lib/libgtest_main.a /usr/local/lib/gtest/libgtest_main.a

