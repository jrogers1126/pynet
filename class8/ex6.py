#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
import django, datetime, threading
def show_arp(device):
    remote_conn = ConnectHandler(device_type=device.device_type,
                                 ip=device.ip_address,
                                 username=device.credentials.username,
                                 password=device.credentials.password,
                                 port=device.port)
    print device.device_name.center(80, '-')
    print remote_conn.send_command('show arp')

def main():
    django.setup()

    start = datetime.datetime.now()
    for device in NetworkDevice.objects.all():
        thread = threading.Thread(target=show_arp, args=(device,))
        thread.start()

    main_thread = threading.currentThread()
    for thread in threading.enumerate():
        if thread != main_thread:
            print thread
            thread.join()
    
    print "Elapsed time: {}".format(datetime.datetime.now() - start)

if __name__ == "__main__":
    main()
