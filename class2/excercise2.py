#!/usr/bin/env pythoTELNET_PORTn
##Import stuff
import pynetlib, telnetlib

#Define stuff
TELNET_PORT=23
TELNET_TIMEOUT=1

def main():
    #Write program here
    telnetlib.Telnet('184.105.247.70', TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
    remote_conn.read_very_eager()
    remote_conn.write('show ip int brief' + '\n')
    remote_conn.close() 

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


