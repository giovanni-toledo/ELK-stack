import os
from autosetup import hostgroups, remote_user
from jinja2 import Environment, FileSystemLoader

# load templates folder 
env = Environment(loader=FileSystemLoader('templates'))

# hosts file
ansible_hosts_file = env.get_template('ansible-hosts').render(hostgroups=hostgroups)

# ansible config
ansible_config_file = env.get_template('ansible.cfg').render(remote_user=remote_user)

# filebeat config
filebeat_config = env.get_template('filebeat-cfg.yml').render(hostgroups=hostgroups)

# metricbeat config
metricbeat_config = env.get_template('metricbeat-cfg.yml').render(hostgroups=hostgroups)

# packetbeat config
packetbeat_config = env.get_template('packetbeat-cfg.yml').render(hostgroups=hostgroups)


# write rendered files

# hosts 
print('writing rendered/hosts')
with open('rendered/hosts', 'w') as f:
    f.write(ansible_hosts_file)


# ansible.cfg
print('writing rendered/ansible.cfg')
with open('rendered/ansible.cfg', 'w') as f:
    f.write(ansible_config_file)

# filebeat.yml
print('writing rendered/filebeat.yml')
with open('rendered/filebeat.yml', 'w') as f:
    f.write(filebeat_config)

# metricbeat.yml
print('writing rendered/metricbeat.yml')
with open('rendered/metricbeat.yml', 'w') as f:
    f.write(metricbeat_config)

# packetbeat.yml
print('writing rendered/packetbeat.yml')
with open('rendered/packetbeat.yml', 'w') as f:
    f.write(packetbeat_config)

