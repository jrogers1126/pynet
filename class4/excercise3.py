#!/usr/bin/env python
#3. Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
import pexpect, getpass, sys, time, re

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass.getpass()
    cmd = 'show ip int brief'
    ssh_conn = pexpect.spawn('ssh {}@{}'.format(username, ip_addr))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 5
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    router_name = ssh_conn.before.strip()
    prompt = router_name + ssh_conn.after.strip()
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect(prompt)
    ssh_conn.sendline(cmd)
    ssh_conn.expect(cmd + '.*' + prompt)
    print ssh_conn.after

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


