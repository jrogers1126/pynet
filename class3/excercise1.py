#!/usr/bin/env python
from __future__ import with_statement, print_function
import pysnmp, snmp_helper, yaml, email_helper, netmiko, time, datetime
'''
    Class 3, Excercise 1 
    Using SNMPv3 create a script that detects router configuration changes.

    If the running configuration has changed, then send an email notification to yourself identifying the router that changed and the time that it changed.

    Note, the running configuration of pynet-rtr2 is changing every 15 minutes (roughly at 0, 15, 30, and 45 minutes after the hour).  This will allow you to test your script in the lab environment. 

    # Uptime when running config last changed
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    SNMPv2-SMI::enterprises.9.9.43.1.1.1.0 = Timeticks: (983457054) 113 days, 19:49:30.54

    # Uptime when running config last saved (note any 'write' constitutes a save)
    ccmHistoryRunningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'
    SNMPv2-SMI::enterprises.9.9.43.1.1.2.0 = Timeticks: (983437639) 113 days, 19:46:16.39

    # Uptime when startup config last saved
    ccmHistoryStartupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
    SNMPv2-SMI::enterprises.9.9.43.1.1.3.0 = Timeticks: (976106481) 112 days, 23:24:24.81

    #sysUptime timestamp (OID sysUptime = 1.3.6.1.2.1.1.3.0)
    DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (983462234) 113 days, 19:50:22.34

    Logic:
    # get running config change timestamp (last_changed_net)
    # Load last checked running config timestamp (last_changed_yaml) from YAML file, default to epoc
    # if last_changed_net > last_changed_yaml, then: get config_net, compare to config_yaml, email diff, store config_net and last_changed_net in yaml file

    To test:
    for min in 16 31 46 61; do echo ./excercise1.py | at now + $min; done
'''
OID_RUN_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_SYSNAME = '.1.3.6.1.2.1.1.5.0'

def get_ios_config(ssh_user=('pyclass', '88newclass'), ip='184.105.247.71'):
    ssh_connect = netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=ssh_user[0], password=ssh_user[1])
    return ssh_connect.send_command("show running-config")

def main():
    # pynet-rtr2 (Cisco 881)
    device = ('184.105.247.71',161)
    snmp_user = ('pysnmp', 'galileo1', 'galileo1')
    ssh_user = ('pyclass', '88newclass')
    recipient = '2016@tybox.net'
    sender = 'config-watcher@py.net'
    device_name = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(device, snmp_user, oid=OID_SYSNAME))
    yaml_filename = device_name + '.yml'
    # get running config change timestamp (last_changed_net)
    last_changed_net = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(device, snmp_user, oid=OID_RUN_CHANGED))
    # Load last checked running config timestamp (last_changed_yaml) from YAML file, default to epoc
    try:
        with open(yaml_filename) as f:
            yaml_data = yaml.load(f)
    except EnvironmentError:
        #Yaml file doesn't exist, load some defaults
        yaml_data = { 'last_changed': 0, 'config': '' }
    # if last_changed_net > last_changed_yaml, then: get config_net, compare to config_yaml, email diff, store config_net and last_changed_net in yaml file
    if last_changed_net > yaml_data['last_changed']:
        print("Change detected. Getting config from " + device_name + "...")
        config_net = get_ios_config().split('\n')
        config_yaml = yaml_data['config']
        config_diff = list(set(config_net).symmetric_difference(set(config_yaml)))
        #Email the difference
        print("Notifying " + recipient + "...")
        subj = 'CHANGE DETECTED: Config on ' + device_name + ' detected at ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        message = 'Previous Config Timestamp: ' + str(yaml_data['last_changed']) + '\n'
        message += 'Current Config Timestamp: ' + last_changed_net + '\n'
        message += '\nNewly Detected Config: \n' 
        message += '\n'.join(config_diff)
        email_helper.send_mail(recipient, subj, message, sender)
        #store the current config and time stamp in yaml file
        print("Storing the current config in " + yaml_filename)
        yaml_data = { 'last_changed': last_changed_net, 'config': config_net }
        with open(yaml_filename, 'w') as f:
            f.write(yaml.safe_dump(yaml_data, default_flow_style=False))
    else:
        print("No change detected")

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


