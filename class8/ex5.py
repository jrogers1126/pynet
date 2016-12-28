#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
import django, datetime

def main():
    django.setup()

    start = datetime.datetime.now()
    for device in NetworkDevice.objects.all():
        remote_conn = ConnectHandler(device_type=device.device_type,
                                     ip=device.ip_address,
                                     username=device.credentials.username,
                                     password=device.credentials.password,
                                     port=device.port)
        print '#' * 80
        print device.device_name, device.vendor
        print remote_conn.send_command('show arp')
    end = datetime.datetime.now() - start
    print "Elapsed time: {}".format(end) 

if __name__ == "__main__":
    main()
