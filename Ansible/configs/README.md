# Ansible configurations

This directory contains templates of the configuration files used by the ansible playbooks to setup the beats.

### Filebeat 

The following changes need to be made to [filebeat-cfg.yml](filebeat-cfg.yml)   
On both instances, `Elk_server_ip` should be the IP of the ELKserver VM
```
output.elasticsearch:
  hosts: ["Elk_server_ip:9200"]
```

```
setup.kibana:
  host: "Elk_server_ip:5601" 
```

### Metricbeat

The following changes need to be made to [metricbeat-cfg.yml](metricbeat-cfg.yml)   
Same as above, `Elk_server_ip` should be replaced with the IP of the ELKserver VM
```
setup.kibana:
  host: "Elk_server_ip:5601"
```

```
output.elasticsearch:
  hosts: ["Elk_server_ip:9200"]
```

### Packetbeat

The following changes need to be made to [packetbeat-cfg.yml](packetbeat-cfg.yml)   
Same as above, `Elk_server_ip` should be replaced with the IP of the ELKserver VM
```
setup.kibana:
  host: "Elk_server_ip:5601"
```

```
output.elasticsearch:
  hosts: ["Elk_server_ip:9200"]
```
