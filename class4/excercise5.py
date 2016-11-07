#!/usr/bin/env python
#5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state (i.e. that you are currently in configuration mode).
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet

def main():
    net_connect = ConnectHandler(**pynet.rtr1)
    print "Entering config mode..."
    print net_connect.config_mode()
    print "In config mode: " + str(net_connect.check_config_mode())
    print "Current Prompt: " + net_connect.find_prompt()

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


