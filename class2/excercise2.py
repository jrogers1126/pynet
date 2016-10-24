#!/usr/bin/env python
##Import stuff
import pynet, telnetlib, time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    #Define stuff
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    login(remote_conn, username, password)
    print( send_cmd(remote_conn, 'show ip int brief') )
    remote_conn.close()

def login(remote_conn, username, password):
    output = remote_conn.read_until('Username:', TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until('Password:', TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def send_cmd(remote_conn, cmd):
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


