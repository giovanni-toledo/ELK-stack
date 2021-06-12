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
    echo -e '[x] failed! \n[!] please install pip3 manually';
    exit;
else
    echo -e '[!] done\n';
fi

# install jinja2
echo '[!] installing jinja2...'
python3 -m pip install jinja2 > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo '[x] failed!';
    exit;
else 
    echo -e '[!] done\n';
fi

# create rendered/
echo '[!] creating rendered/'
mkdir rendered

# render config files
echo -e '[!] rendering configuration files...\n'
python3 render.py 

# configure ansible
echo '[!] configuring ansible...'
cp rendered/ansible.cfg /etc/ansible/ansible.cfg
cp rendered/hosts /etc/ansible/hosts
echo -e '[!] done\n'

# insert elastic beats configuration templates in Ansible/configs
echo '[!] populating Ansible/configs'
cp rendered/*beat.yml ../Ansible/configs/
echo -e 'done\n'

