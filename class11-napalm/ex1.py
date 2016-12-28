#!/usr/bin/env python
from napalm import get_network_driver
import devices

def main():
    device_list = [
        devices.rtr1,
        devices.rtr2,
        devices.sw1,
        devices.sw2,
        devices.srx1,
        #devices.srx2,
    ]
    for a_device in device_list:
        #Remove the merge_file if it is there, we don't need it until ex2
        a_device.pop('merge_file', None)
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)
        print a_device['hostname'].center(80, '-')
        device.open()
        device_facts = device.get_facts()
        print "{hostname}: Model={model}".format(**device_facts)

    print

if __name__ == "__main__":
    main()
