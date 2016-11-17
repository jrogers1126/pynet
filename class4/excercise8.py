#!/usr/bin/env python
#8. Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2 (see 'Errata and Other Info, item #4).
#4. Netmiko supports a method (send_config_from_file) that allows you to execute configuration commands directly from a file. For example, if you had a set of commands in a file called 'config_file.txt', then you could execute those commands via the SSH channel as follows:
#             net_connect.send_config_from_file(config_file='config_file.txt')
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet, random

def main():
    rtr1 = ConnectHandler(**pynet.rtr1)
    rtr2 = ConnectHandler(**pynet.rtr2)
    print pynet.horizontal_rule( "Current rtr1 config" )
    print rtr1.send_command('show run | inc logging')
    print pynet.horizontal_rule("Entering config mode and applying config in ./excercise8-config" )
    rtr1.config_mode()
    rtr1.send_config_from_file(config_file='excercise8-config')
    print pynet.horizontal_rule( "New rtr1 config" )
    rtr1.exit_config_mode()
    print rtr1.send_command('show run | inc logging')
    print pynet.horizontal_rule( "Current rtr2 config" )
    print rtr2.send_command('show run | inc logging')
    print pynet.horizontal_rule("Entering config mode and applying config in ./excercise8-config" )
    rtr2.config_mode()
    rtr2.send_config_from_file(config_file='excercise8-config')
    print pynet.horizontal_rule( "New rtr2 config" )
    rtr2.exit_config_mode()
    print rtr2.send_command('show run | inc logging')

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


