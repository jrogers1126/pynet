#!/usr/bin/env python
##Import stuff
from snmp_helper import snmp_get_oid, snmp_extract
import pynet

COMMUNITY='galileo'
SNMP_PORT=161

def main():
    sysName = '.1.3.6.1.2.1.1.5.0'
    sysDescr = '.1.3.6.1.2.1.1.1.0'
    rtr1=('184.105.247.70', COMMUNITY, SNMP_PORT)
    rtr2=('184.105.247.71', COMMUNITY, SNMP_PORT)
    pynet.hr("pynet-rtr1")
    print('SysName: ' + snmp_extract(snmp_get_oid(rtr1, oid=sysName)))
    print('SysDescr: ' + snmp_extract(snmp_get_oid(rtr1, oid=sysDescr))).splitlines()[0]
    pynet.hr("pynet-rtr2")
    print('SysName: ' + snmp_extract(snmp_get_oid(rtr2, oid=sysName)))
    print('SysDescr: ' + snmp_extract(snmp_get_oid(rtr2, oid=sysDescr))).splitlines()[0]


##Only run if not called by another file/program
if __name__ == "__main__":
    main()


