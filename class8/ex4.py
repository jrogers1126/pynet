#!/usr/bin/env python
from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    NetworkDevice.objects.filter(device_name='pynet-srx9').delete()
    NetworkDevice.objects.filter(device_name='pynet-sw9').delete()

    print NetworkDevice.objects.all()

if __name__ == "__main__":
    main()
