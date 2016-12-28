#!/usr/bin/env python
'''
Using NAPALM and the one of the Cisco routers perform the following config operations:
a. Stage a change adding a /32 static route (merge operation). Use something in 1.1.X.X/32.
b. Perform a compare_config operation to see your staged change.
c. Discard your change.
d. Verify compare_config shows no pending changes (after your discard operation).
e. Re-stage your change adding a /32 static route (merge operation).
f. Commit your change.
'''
from napalm import get_network_driver
import devices

devices = (devices.rtr1,)
napalm_conns = []
for a_device in devices:
    device_type = a_device.pop('device_type', 'ios')
    merge_file = a_device.pop('merge_file')
    driver = get_network_driver(device_type)
    device = driver(**a_device)
    napalm_conns.append(device)
    print a_device['hostname'].center(80, '=')
    device.open()
    print "Load config change (merge) - no commit".center(80, '-')
    device.load_merge_candidate(filename=merge_file)
    print device.compare_config()
    
    print "Discarding config change".center(80, '-')
    device.discard_config()

    print "Another compare operation".center(80, '-')
    print device.compare_config()

    print "Load config change (merge) - with commit".center(80, '*')
    device.load_merge_candidate(filename=merge_file)
    print device.compare_config()
    device.commit_config()
    
