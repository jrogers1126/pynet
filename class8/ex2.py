#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    for device in NetworkDevice.objects.all():
        if 'cisco' in device.device_type:
            device.vendor = 'Cisco'
        elif 'juniper' in device.device_type:
            device.vendor = 'Juniper'
        elif 'arista' in device.device_type:
            device.vendor = 'Arista'
        print device.device_name, device.vendor
        device.save()

if __name__ == "__main__":
    main()
