#!/usr/bin/env sh

apt-get purge apache2 apache2-utils
apt-get install apache2
apt-get install openssl

a2enmod ssl

# rm /etc/apache2/sites-enabled/000-default.conf
# ln -s ../default.ssl.conf /etc/apache2/sites-enabled/ssl.conf
cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/ssl.conf
cp files/virtualhost.conf /etc/apache2/sites-enabled/virtualhost.conf

# service apache2 restart

# ====================
echo 'Apache2 with SSL ok.'
echo 'Now set SSL to vulnerable setting'
# ====================

mkdir /etc/apache2/ssl
# sudo openssl req -new -x509 -days 365 -nodes -out /etc/apache2/ssl/apache.pem -keyout /etc/apache2/ssl/apache.key
openssl dhparam -out /etc/apache2/ssl/dhparams512.pem 512
cp files/ssl.conf /etc/apache2/mods-enabled/ssl.conf

apt-get install php libapache2-mod-php

# ====================
echo 'Set SSL to vulnerable setting ok'
echo 'Now copy website'
# ====================

cp www/* /var/www/html/
rm /var/www/html/index.html

service apache2 restart

echo 'done'
