#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
from netmiko import ConnectHandler
import django, datetime, multiprocessing
def show_arp(device, q):
    output_dict = {}
    remote_conn = ConnectHandler(device_type=device.device_type,
                                 ip=device.ip_address,
                                 username=device.credentials.username,
                                 password=device.credentials.password,
                                 port=device.port,
                                 verbose=False)
    output = device.device_name.center(80, '-')
    output += "\n"
    output += remote_conn.send_command('show arp')
    output_dict[device.device_name] = output
    q.put(output_dict)


def main():
    django.setup()

    start = datetime.datetime.now()
    procs = []
    q = multiprocessing.Queue(maxsize=20)
    
    for device in NetworkDevice.objects.all():
        proc = multiprocessing.Process(target=show_arp, args=(device, q))
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()
    
    while not q.empty():
        for k,v in q.get().iteritems():
            print v

    print "Elapsed time: {}".format(datetime.datetime.now() - start)

if __name__ == "__main__":
    main()
