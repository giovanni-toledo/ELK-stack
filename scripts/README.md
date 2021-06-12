## Auto-install scripts

This directory contains scripts used to automate the setup and deployment of the network. 
Below is a description of each file.

### hosts.py

This file is the only one that may need to be edited to match the network configuration.   
It is imported by render.py and the objects are used to render the hosts and configuration files for ansible, and elasticsearch beats.
It contains the following:
```
hostgroups = [
    {
        'name' : 'webservers',
        'hosts' : [
            '10.0.0.8',
            '10.0.0.9',
            '10.0.0.10'
        ]
    },
    {
        'name' : 'elk',
        'hosts' : '10.1.0.4'
    }
]
```
- `hostgroups` is a list of python objects. 
- These objects are used to render:
    - `/etc/ansible/hosts`
    - the elasticsearch beats configuration files


```
remote_user = 'azadmin'
```
- Used to edit:
    - /etc/ansible/ansible.cfg

### render.py

This script:
- imports the data from hosts.py
- uses jinja2 to render the configuration files from the templates found in [templates](templates).
- writes the rendered files to the `rendered/` directory
    - `rendered/` is created by `setup.sh` and does not exist by default
    - execution fails if `rendered/` is not present
 

### setup.sh

This script:
- must be run as root
- `./setup.sh`
- installs dependencies:
    - pip3
    - jinja2
- runs the setup
    - creates the `rendered/` directory
    - calls `render.py`
    - overwrites:
        - `/etc/ansible/hosts` with `rendered/hosts`
        - `/etc/ansible/ansible.cfg` with `rendered/ansible.cfg`
        - all the beat configuration files in `Elk-stack/Ansible/configs`
- runs the playbooks
    - `./setup.sh install`
    - runs `elk-playbook.yml`
    - runs `dvwa-playbook.yml`
    - runs `beats-playbook.yml`
