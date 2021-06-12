'''
This file is imported by render.py and uses the variables below to render configuration files with jinja
Edit objects to match network setup
'''

# Edit the following lines to match the Web and Elk machines
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


# If SSH keys configured, uncomment and edit the line below to match the username 
remote_user = 'azadmin'
