#!/bin/bash

# check for root 
if [ $UID -ne 0 ]; then
    echo 'Please run as root!';
    exit;
fi

# install python3-pip
echo '[!] installing pip3...' 
apt update > /dev/null 2>&1
apt install python3-pip -y > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo '[x] failed! \n[!] please install pip3 manually';
    exit;
else
    echo '[!] success';
fi

# install jinja2
echo '[!] installing jinja2...'
python3 -m pip install jinja2 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo '[x] failed!';
    exit;
else 
    echo '[!] success';
fi


# render config files
echo '[!] rendering configuration files...'
python3 render.py 

