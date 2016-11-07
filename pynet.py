#!/usr/bin/env python
#A library of stuff to use

#import stuff
from pysnmp.entity.rfc3413.oneliner import cmdgen
""" 
    passwords.py is stored locally, and not in git for security reasons. 
    It contains only one line:
    passwords = [ 'firstpass', 'secondpass', 'maybeathird', 'etc' ]
"""
import passwords

def horizontal_rule(msg, character='#'):
    #not worth figuring the term width cross-platform, assume 80
    width = 80
    return " {} ".format(msg.strip()).center(width, character)

rtr1 = { 
    #model: Cisco 881
    'ip': '184.105.247.70',
    'port': 22,
    'username': 'pyclass',
    'device_type': 'cisco_ios',
    'password': passwords.passwords[0],
}

rtr2 = {
    #model: Cisco 881
    'ip': '184.105.247.71',
    'port': 22,
    'username': 'pyclass',
    'device_type': 'cisco_ios',
    'password': passwords.passwords[0]
}

sw1 = {
    #'model': 'Arista vEOS switch',
    'ip': '184.105.247.72',
    'port': 22,
    #'eapi_port': 443,
    'username': 'admin1',
    'device_type': 'arista_eos',
    'password': passwords.passwords[1]
}

sw2 = {
    #'model': 'Arista vEOS switch',
    'ip': '184.105.247.73',
    'port': 22,
    #'eapi_port': 443,
    'username': 'admin1',
    'device_type': 'arista_eos',
    'password': passwords.passwords[1]
}

sw3 = {
    #'model': 'Arista vEOS switch',
    'ip': '184.105.247.74',
    'port': 22,
    #'eapi_port': 443,
    'username': 'admin1',
    'device_type': 'arista_eos',
    'password': passwords.passwords[1]
}

sw4 = {
    #'model': 'Arista vEOS switch',
    'ip': '184.105.247.75',
    'port': 22,
    #'eapi_port': 443,
    'username': 'admin1',
    'device_type': 'arista_eos',
    'password': passwords.passwords[1]
}

srx1 = {
    #'model': 'Juniper SRX',
    'ip': '184.105.247.76',
    'port': 22,
    #'netconf_port': 830,
    'username': 'pyclass',
    'device_type': 'juniper',
    'password': passwords.passwords[0]
}


