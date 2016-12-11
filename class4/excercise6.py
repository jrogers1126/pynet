#!/usr/bin/env python
#6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet

arp_map = {"cisco_ios": "show ip arp",
           "juniper": "show arp no-resolve"}
           
def main():
    for device in (pynet.rtr1, pynet.rtr2, pynet.srx1):
        device_handler = ConnectHandler(**device) 
        print (" " + device['ip'] + " ").center(80, "*")
        print device_handler.find_prompt() + device['device_type']
        print device_handler.send_command(arp_map[device['device_type']])
        print ""
 
##Only run if not called by another file/program
if __name__ == "__main__":
    main()


