#!/usr/bin/env sh
sudo apt-get install libpcre3 libpcre3-dev gcc g++ make

INSTALL_PATH=$HOME/apache
BIN_PATH=$INSTALL_PATH/local
APR_BIN_PATH=$BIN_PATH/apr
APR_UTIL_BIN_PATH=$BIN_PATH/apr-util
HTTPD_BIN_PATH=$BIN_PATH/httpd

mkdir $INSTALL_PATH
cd $INSTALL_PATH

wget http://ftp.mirror.tw/pub/apache//apr/apr-1.5.2.tar.gz
wget http://ftp.tc.edu.tw/pub/Apache//apr/apr-util-1.5.4.tar.gz
wget https://archive.apache.org/dist/httpd/httpd-2.4.1.tar.gz

tar -xzvf apr-1.5.2.tar.gz
tar -xzvf apr-util-1.5.4.tar.gz
tar -xzvf httpd-2.4.1.tar.gz

cd apr-1.5.2
./configure --prefix=$APR_BIN_PATH
make && make install
make clean
cd ../

cd apr-util-1.5.4
./configure --prefix=$APR_UTIL_BIN_PATH --with-apr=$APR_BIN_PATH
make && make install
make clean
cd ../

cd httpd-2.4.1
./configure --prefix=$HTTPD_BIN_PATH --with-apr=$APR_BIN_PATH --with-apr-util=$APR_UTIL_BIN_PATH
make && make install
make clean
cd ../

echo 'maybe done'
echo "install in $HTTPD_BIN_PATH"

