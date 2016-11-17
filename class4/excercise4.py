#!/usr/bin/env python
#4. Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
import pexpect, getpass, sys, time, re, random

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass.getpass()
    buffersize = random.randrange(4096, 9096)
    cmd = 'logging buffered ' + str(buffersize)
    ssh_conn = pexpect.spawn('ssh {}@{}'.format(username, ip_addr))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 5
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    router_name = ssh_conn.before.strip()
    prompt = router_name + ssh_conn.after.strip()
    ssh_conn.sendline('conf t')
    ssh_conn.expect_exact('(config)#')
    ssh_conn.sendline(cmd)
    ssh_conn.expect(router_name)
    ssh_conn.sendline('do show run | include logging buffered')
    ssh_conn.expect(router_name)
    print ssh_conn.before

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


