## Auto-install scripts

This directory contains scripts used to automate the setup and deployment of the network. 
Below is a description of each file.

### setup.sh

This script:
- Must be run as root
- `./setup.sh`
- Installs dependencies:
    - pip3
    - jinja2
- Runs the setup
    - Creates the `rendered/` directory
    - Calls `render.py`
    - Overwrites:
        - `/etc/ansible/hosts` with `rendered/hosts`
        - `/etc/ansible/ansible.cfg` with `rendered/ansible.cfg`
        - All the beat configuration files in `Elk-stack/Ansible/configs`
- `./setup.sh install`
    - Runs `elk-playbook.yml`
    - Runs `dvwa-playbook.yml`
    - Runs `beats-playbook.yml`


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
    - The elasticsearch beats configuration files


```
remote_user = 'azadmin'
```
- Used to edit:
    - /etc/ansible/ansible.cfg

### render.py

This script:
- Imports the data from hosts.py
- Uses jinja2 to render the configuration files from the templates found in [templates](templates).
- Writes the rendered files to the `rendered/` directory
    - `rendered/` is created by `setup.sh` and does not exist by default
    - Execution fails if `rendered/` is not present
 
