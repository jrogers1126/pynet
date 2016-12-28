#!/usr/bin/env python
"""
Connect to set of network devices using NAPALM (different platforms); print
out the facts.
"""
from napalm import get_network_driver
import pynet
from getpass import getpass

def main():
    """
    Connect to set of network devices using NAPALM (different platforms); print
    out the facts.
    """
    device_list = [
        pynet.rtr1,
        pynet.rtr2,
        pynet.sw1,
        pynet.sw2,
        pynet.srx1,
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
