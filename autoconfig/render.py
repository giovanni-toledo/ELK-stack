import os
import hosts
from jinja2 import Environment, FileSystemLoader

# load templates folder 
env = Environment(loader=FileSystemLoader('templates'))

# hosts file
ansible_hosts_file = env.get_template('ansible-hosts').render(hostgroup=hosts.hostgroups)
print('[!] writing rendered/hosts')
with open('rendered/hosts', 'w+') as f:
    f.write(ansible_hosts_file)

# ansible config
if hosts.remote_user:
    ansible_config_file = env.get_template('ansible.cfg').render(remote_user=hosts.remote_user)
    print('[!] writing rendered/ansible.cfg')
    with open('rendered/ansible.cfg', 'w') as f:
        f.write(ansible_config_file)
else:
    pass

# filebeat config
filebeat_config = env.get_template('filebeat-cfg.yml').render(hostgroup=hosts.hostgroups)
print('[!] writing rendered/filebeat.yml')
with open('rendered/filebeat.yml', 'w') as f:
    f.write(filebeat_config)

# metricbeat config
metricbeat_config = env.get_template('metricbeat-cfg.yml').render(hostgroup=hosts.hostgroups)
print('[!] writing rendered/metricbeat.yml')
with open('rendered/metricbeat.yml', 'w') as f:
    f.write(metricbeat_config)

# packetbeat config
packetbeat_config = env.get_template('packetbeat-cfg.yml').render(hostgroup=hosts.hostgroups)
print('[!] writing rendered/packetbeat.yml')
with open('rendered/packetbeat.yml', 'w') as f:
    f.write(packetbeat_config)

