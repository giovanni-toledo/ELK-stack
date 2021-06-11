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


# If SSH keys configured, edit the line below to match the username as follows:
# remote_user = 'azadmin'
remote_user = None