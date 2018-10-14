#This script is still untested. Run individual commands based in the link below
#https://wiki.qt.io/Install_Qt_5_on_Ubuntu

#This script installs Qt on fresh ubuntu installation,
#Run this script in the directory ~/qtcreator/
QT_FILE_NAME=qt-opensource-linux-x64-5.11.2.run
wget http://download.qt.io/official_releases/qt/5.11/5.11.2/${QT_FILE_NAME}

chmod +x ${QT_FILE_NAME}

./${QT_FILE_NAME}

sudo apt-get install build-essential

sudo apt-get install libfontconfig1

sudo apt-get install mesa-common-dev

sudo apt-get install libglu1-mesa-dev -y


