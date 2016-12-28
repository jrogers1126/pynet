#!/usr/bin/env python
from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()

    pynet_rtr9 = NetworkDevice(
        device_name='pynet-srx9',
        device_type='juniper',
        vendor='Juniper',
        credentials=Credentials.objects.all()[0],
        ip_address='184.105.247.254',
        port=22,
    )
    pynet_rtr9.save()
    print pynet_rtr9

    pynet_sw9 = NetworkDevice.objects.get_or_create(
        device_name='pynet-sw9',
        device_type='arista_eos',
        vendor='Arista',
        credentials=Credentials.objects.all()[1],
        ip_address='184.105.247.253',
        port=22,
    )
    print pynet_sw9


if __name__ == "__main__":
    main()
