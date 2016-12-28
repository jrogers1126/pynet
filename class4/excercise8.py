#!/usr/bin/env python
'''
#8. Use Netmiko to change the logging buffer size (logging buffered <size>) 
and to disable console logging (no logging console) from a file on both pynet-rtr1 
and pynet-rtr2 (see 'Errata and Other Info, item #4).
#4. Netmiko supports a method (send_config_from_file) that allows you to execute 
configuration commands directly from a file. For example, if you had a set of 
commands in a file called 'config_file.txt', then you could execute those commands
via the SSH channel as follows:
'''
#             net_connect.send_config_from_file(config_file='config_file.txt')
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet, random


def main():
    for device in (pynet.rtr1, pynet.rtr2):
        device_handler = ConnectHandler(**device) 
        print (" Current config for " + device['ip'] + " ").center(80, "*")
        print device_handler.send_command('show run | inc logging')
        print (" Entering config mode and applying config in ./excercise8-config ").center(80, "*")
        device_handler.config_mode()
        device_handler.send_config_from_file(config_file='excercise8-config')
        print (" New config for " + device['ip'] + " ").center(80, "*")
        device_handler.exit_config_mode()
        print device_handler.send_command('show run | inc logging')
        print

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


