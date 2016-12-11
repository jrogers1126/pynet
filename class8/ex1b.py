#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    for device in NetworkDevice.objects.all():
        if device.device_type == 'arista_eos':
            device.credentials = Credentials.objects.all()[1]
        else:
            device.credentials = Credentials.objects.all()[0]
        print device.device_name, device.credentials
        device.save()

if __name__ == "__main__":
    main()
