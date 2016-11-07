#!/usr/bin/env python
#9. Bonus Question - Redo exercise6 but have the SSH connections happen concurrently using either threads or processes (see example). What main issue is there with using threads in Python?
##Import stuff
from netmiko import ConnectHandler
#pynet.py is found in root git directory
import pynet, multiprocessing

def showCommand(hostname, cmd):
    """
        This is causing the output of multiple processes to 'walk on one another', a better way to do this would be to output this to a global variable
        that could be printed later.  I'm not tackling that because I'm short on time.  Here is a rough example of of the for statement to wait for
        processes to finish:
            for j in jobs:
                j.join()
                print j.output
        The problem is a job doens't have a method 'output' or anything like it.  Not sure how to get it from the worker function (showCommand) to 
        outside the process management
    """
    net_connect = ConnectHandler(**eval('pynet.' + hostname))
    pynet.horizontal_rule(hostname)
    print net_connect.find_prompt() + cmd
    print net_connect.send_command(cmd)
    return

##Only run if not called by another file/program
if __name__ == "__main__":
    ios_arp = "show ip arp"
    junos_arp = "show arp no-resolve"
    devices = [
        { 'hostname': 'rtr1', 'cmd': ios_arp },
        { 'hostname': 'rtr2', 'cmd': ios_arp },
        { 'hostname': 'srx1', 'cmd': junos_arp },
    ]
    jobs = []
    for device in devices:
        p = multiprocessing.Process(target=showCommand, args=(device['hostname'],device['cmd'],))
        jobs.append(p)
        p.start()


