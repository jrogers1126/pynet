#!/usr/bin/env python
##Write some stuff to files
import yaml, json

d = { 'hostname': 'router1', 'ip_address': '1.2.3.4',
    'interfaces': [ 'ge-0/0/0', 'ge-0/0/1', 'ge-0/0/2', 'ge-0/0/3'] }


#Write it out to YAML file
with open("week1.yaml", "w") as f:
    f.write(yaml.dump(d, default_flow_style=False))

#Write it out to json file
with open("week1.json", "w") as f:
    f.write(json.dump(d, f))
