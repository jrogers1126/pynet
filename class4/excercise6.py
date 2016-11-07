#!/usr/bin/env python
#6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet

def main():
    ios_arp = "show ip arp"
    junos_arp = "show arp no-resolve"
    rtr1 = ConnectHandler(**pynet.rtr1)
    rtr2 = ConnectHandler(**pynet.rtr2)
    srx1 = ConnectHandler(**pynet.srx1)
    print pynet.horizontal_rule("rtr1")
    print rtr1.find_prompt() + ios_arp
    print rtr1.send_command(ios_arp)
    print pynet.horizontal_rule("rtr2")
    print rtr2.find_prompt() + ios_arp
    print rtr1.send_command(ios_arp)
    print pynet.horizontal_rule("srx1")
    print srx1.find_prompt() + junos_arp
    print srx1.send_command(junos_arp)

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


