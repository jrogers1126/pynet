#!/usr/bin/env python
#7. Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet, random

def main():
    buffersize = random.randrange(4096, 9096) 
    net_connect = ConnectHandler(**pynet.rtr2)
    pynet.horizontal_rule( "Checking current config" )
    print net_connect.send_command('show run | inc logging')
    pynet.horizontal_rule("Entering config mode and changing config" )
    net_connect.config_mode()
    net_connect.send_command('logging buffered ' + str(buffersize))
    pynet.horizontal_rule( "checking new config" )
    net_connect.exit_config_mode()
    print net_connect.send_command('show run | inc logging')

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


