import hosts
from jinja2 import Environment, FileSystemLoader

'''
This file contains 2 main functions: 
render_file renders multiple configuration files from jinja2 templates located in templates/ and writes the rendered file in rendered/
edit_cfg is a more straightforward approach to editing templates/ansible.cfg since it was not playing nice with jinja2, and also writes it to rendered/

variables for the templates are imported from hosts.py
'''

# load templates folder 
env = Environment(loader=FileSystemLoader('templates'))

def render_file(file_template, variable):
    # put rendered file into a variable
    render = env.get_template(file_template).render(var=variable)
    # some output
    print(f'[+] writing rendered/{file_template}')
    # open file handler
    with open(f'rendered/{file_template}', 'w') as f:
        # write rendered file to redered/<filename>
        f.write(render)


# ansible.cfg isn't playing nice with jinja
def edit_cfg():
    # specific for ansible.cfg
    filename = 'ansible.cfg'
    # empty list to store each line in file
    lines = []
    # position of line to replace
    position = 105
    # test
    line = f'remote_user = {hosts.remote_user}'
    # file handler, read mode
    with open(f'templates/{filename}', 'r') as f:
        # store each line in lines  
        lines = f.readlines()
    # remove existing line
    lines.remove(lines[position])
    # insert line
    lines.insert(position, line)
    # some output
    print(f'[+] writing rendered/{filename}')
    # file handler, write mode
    with open(f'rendered/{filename}', 'w') as f:
        # write every line in edited file 
        for line in lines:
            f.write(line)

# hosts file
render_file('hosts', hosts.hostgroups)
# edit config if the remote_user is set in hosts.py
if hosts.remote_user:
    edit_cfg()
else:
    pass
# filebeat
render_file('filebeat.yml', hosts.hostgroups)
# metricbeat
render_file('metricbeat.yml', hosts.hostgroups)
# packetbeat 
render_file('packetbeat.yml', hosts.hostgroups)





