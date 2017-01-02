# MitM-SSL-server-demo
NTU NS 2016 final project. Perform a Man in the Middle attack to a old Apache httpd 2.4.1. It's a implementation of [logjam]

## Test Environment
- Ubuntu Server 16.04 LTS
 - VM disk size > 4GB
- apache2 2.4.18

## Progess

- [X] install apache httpd
- [X] configure ssl setting
- [X] set up sample site
- [ ] logjam to apache

## Usage

    sudo ./run.sh

 This will REMOVE OLD *apache2* and */var/www/html*

 - To download a vulnerable browser: check [browser history wiki]. 
 - [vulnerable opera windows]
 - [vulnerable opera osx]
 - [firefox cipher viewer]
 - [old vulnerable firefox] \(I Can't install old osx version QQ\)
 - Remember to close auto update of these old browser

    sudo ./MitM.py
    
 - Create MitM listening port 81
 
    ./read_handshake.py

 - read handshake protocol 

## Methods

 - Configure Apache in an inversed way mentioned in this [article](http://serverfault.com/questions/693241/how-to-fix-logjam-vulnerability-in-apache-httpd)
 - produce vulnerable Diffie-Hellman parameter by `sudo openssl dhparam -out /etc/apache2/dhparams512.pem 512`
 - Change CipherSuites in ClientHello (handshake) ([by this](http://blog.fourthbit.com/2014/12/23/traffic-analysis-of-an-ssl-slash-tls-session)) to DHE\_EXPORT


[logjam]: https://weakdh.org/logjam.html "Logjam"
[browser history wiki]: https://en.wikipedia.org/wiki/Template:TLS/SSL_support_history_of_web_browsers "browser history"
[vulnerable opera windows]: http://www.opera.com/download/guide/?os=windows&ver=28.0.1750.40&local=y "Vulnerable Opera for windows"
[vulnerable opera osx]: http://www.opera.com/download/guide/?os=osx&ver=28.0.1750.40&local=y "Vulnerable Opera for osx"
[firefox cipher viewer]: https://addons.mozilla.org/en-US/firefox/addon/cipherfox/ "Firefox cipher detail viewer extension"
[old vulnerable firefox]: https://ftp.mozilla.org/pub/firefox/releases/34.0/ 

