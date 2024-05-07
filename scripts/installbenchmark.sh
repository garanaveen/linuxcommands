THIRDPARTY_TOOLS_DIR=${HOME}/thirdpartytools
GBENCH_SOURCE_DIR=${THIRDPARTY_TOOLS_DIR}/benchmark
GBENCH_BUILD_DIR=${GTEST_SOURCE_DIR}/build


mkdir ${THIRDPARTY_TOOLS_DIR}



# Check out the library.
git clone git@github.com:google/benchmark.git  ${GBENCH_SOURCE_DIR}
# Go to the library root directory
cd ${GBENCH_SOURCE_DIR}
# Make a build directory to place the build output.
cmake -E make_directory "build"


# Generate build system files with cmake, and download any dependencies.
cmake -E chdir "build" cmake -DBENCHMARK_DOWNLOAD_DEPENDENCIES=on -DCMAKE_BUILD_TYPE=Release ../

# or, starting with CMake 3.13, use a simpler form:
# cmake -DCMAKE_BUILD_TYPE=Release -S . -B "build"
# Build the library.
cmake --build "build" --config Release


# Run the tests to check the build.
cmake -E chdir "build" ctest --build-config Release

# Install the library globally,
sudo cmake --build "build" --config Release --target install

