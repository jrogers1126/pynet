#!/usr/bin/env python
#1. Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 

##Import stuff
import paramiko, time
from getpass import getpass

def main():
    #Write program here
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.send("term length 0\nshow version\n")
    time.sleep(1)
    outp = remote_conn.recv(5000) 
    print outp

##Only run if not called by another file/program
if __name__ == "__main__":
    main()

