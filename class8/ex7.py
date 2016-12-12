#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
import django, datetime, multiprocessing
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
    procs = []
    for device in NetworkDevice.objects.all():
        proc = multiprocessing.Process(target=show_arp, args=(device,))
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()
    
    print "Elapsed time: {}".format(datetime.datetime.now() - start)

if __name__ == "__main__":
    main()
