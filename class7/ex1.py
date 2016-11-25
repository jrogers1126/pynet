#!/usr/bin/env python
import pyeapi
#pynet.py is in ~/pylib https://github.com/jrogers512/pynet/blob/master/pynet.py
import pynet 

sw2 = pyeapi.connect_to('pynet-sw2')

interfaces = sw2.enable("show interfaces")[0]['result']['interfaces']
for interface in interfaces:
    if 'interfaceCounters' in interfaces[interface]:
        print pynet.horizontal_rule(interface, '-')
        #print "    bandwidth: " + str(interfaces[interface]['bandwidth']) 
        print "     inOctets: " + str(interfaces[interface]['interfaceCounters']['inOctets'])
        print "    outOctets: " + str(interfaces[interface]['interfaceCounters']['outOctets'])
        print ""
    
