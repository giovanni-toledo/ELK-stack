#!/bin/bash

# Script to install dependencies, set up ansible, render configuration files 
# to run the setup:
#   sudo ./setup.sh 
# to run the setup AND run the playbooks 
#   sudo ./setup.sh install


# check for root 
if [ $UID -ne 0 ] then
    echo 'Please run as root!'
    exit
fi

# install python3-pip
echo '[!] installing pip3...' 
apt update > /dev/null 2>&1
apt install python3-pip -y > /dev/null 2>&1
if [ $? -ne 0 ] then
    echo -e '[x] failed! \n[!] please install pip3 manually'
    exit
else
    echo -e '[+] done\n'
fi

# install jinja2
echo '[!] installing jinja2...'
python3 -m pip install jinja2 > /dev/null 2>&1
if [ $? -ne 0 ] then
    echo '[x] failed!'
    exit
else 
    echo -e '[+] done\n'
fi

# create rendered/
echo '[!] creating rendered/'
mkdir rendered 2>/dev/null

# render config files
echo '[!] rendering configuration files...'
echo '[!] python3 render.py'
python3 render.py 

# configure ansible
echo -e  '\n[!] configuring ansible...'
cp rendered/ansible.cfg /etc/ansible/ansible.cfg
cp rendered/hosts /etc/ansible/hosts
echo -e '[+] done\n'

# insert elastic beats configuration templates in Ansible/configs
echo '[!] populating Ansible/configs'
cp rendered/*beat.yml ../Ansible/configs/
echo -e '[+] done\n'

echo -e '\n[+] SETUP COMPLETE\n'

# if ./setup.sh install 
if [ ! -z $1 ] && [ $1 = 'install' ] then
    echo -e '[!] Running Playbooks\n'
    cd ../Ansible/playbooks
    # install elk server first
    # beat playbooks fail if kibana is not ready
    ansible-playbook elk-playbook.yml
    # install dvwa
    ansible-playbook dvwa-playbook.yml
    # install beats
    ansible-playbook beats-playbook.yml
fi

echo 'Goodbye...'
