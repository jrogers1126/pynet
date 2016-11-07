#!/usr/bin/env python
#9. Bonus Question - Redo exercise6 but have the SSH connections happen concurrently using either threads or processes (see example). What main issue is there with using threads in Python?
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet, multiprocessing

def showCommand(hostname, net_connect, cmd):
    print net_connect.find_prompt() + cmd
    print net_connect.send_command(cmd)
    return

##Only run if not called by another file/program
if __name__ == "__main__":
    ios_arp = "show ip arp"
    junos_arp = "show arp no-resolve"
    rtr1 = ConnectHandler(**pynet.rtr1)
    rtr2 = ConnectHandler(**pynet.rtr2)
    srx1 = ConnectHandler(**pynet.srx1)
    devices = [
        { 'hostname': 'rtr1', 'net_connect': rtr1, 'cmd': ios_arp },
        { 'hostname': 'rtr2', 'net_connect': rtr2, 'cmd': ios_arp },
        { 'hostname': 'srx1', 'net_connect': srx1, 'cmd': junos_arp },
    ]
    jobs = []
    for device in devices:
        p = multiprocessing.Process(target=showCommand, args=(device['hostname'],device['net_connect'],device['cmd'],))
        jobs.append(p)
        p.start()


