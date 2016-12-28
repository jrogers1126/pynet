#!/usr/bin/env python
"""
Connect to set of network devices using NAPALM (different platforms); print
out the facts.
"""
from napalm import get_network_driver
from getpass import getpass

def main():
    """
    Connect to set of network devices using NAPALM (different platforms); print
    out the facts.
    """

    std_pwd = getpass("Enter standard password: ")
    arista_pwd = getpass("Enter Arista password: ")

    srx2 = {
            'hostname': '127.0.0.1',
            'username': 'pyclass',
            'device_type': 'juniper',
            'password': std_pwd,
            'optional_args': {
                'port': 2222
            }    
    }

    device_list = [
        #rtr1,
        #rtr2,
        #sw1,
        #sw2,
        #srx1,
        srx2,
    ]
    for a_device in device_list:
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        print ">>>Opening {}".format(a_device['ip'])
        device.open()
        print "-" * 50
        device_facts = device.get_facts()
        print "{hostname}: Model={model}".format(**device_facts)

    print

if __name__ == "__main__":
    main()
