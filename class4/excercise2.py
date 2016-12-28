#!/usr/bin/env python
#2. Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. 
#This will require that you enter into configuration mode.

##Import stuff
import paramiko, time, random
from getpass import getpass

def main():
    #Write program here
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    buffersize = random.randrange(4096, 9096) 
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
    remote_conn_pre.connect(ip_addr, username=username, password=password, 
                            look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.settimeout(4.0)
    remote_conn.send("term length 0\n")
    remote_conn.send("show version\n")
    remote_conn.send("conf t\n")
    remote_conn.send("logging buffered " + str(buffersize) + "\n")
    remote_conn.send("exit\n")
    time.sleep(1)
    outp = remote_conn.recv(5000) 
    print outp

##Only run if not called by another file/program
if __name__ == "__main__":
    main()

