#!/usr/bin/env python
'''
convert https://raw.githubusercontent.com/ktbyers/pynet/master/pyth_ans_ecourse/class2/ex2_telnetlib.py from functions to a class
'''

import telnetlib, time, socket, sys, getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class Router:
    def __init__(self):
        pass

    def send_command(self, remote_conn, cmd):
        '''
        Send a command down the telnet channel

        Return the response
        '''
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

    def login(self, remote_conn, username, password):
        '''
        Login to network device
        '''
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output

    def disable_paging(self, remote_conn, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(remote_conn, paging_cmd)

    def telnet_connect(self, ip_addr):
        '''
        Establish telnet connection
        '''
        try:
            return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    pynet_rtr1 = Router()
    remote_conn = pynet_rtr1.telnet_connect(ip_addr)
    output = pynet_rtr1.login(remote_conn, username, password)

    time.sleep(1)
    remote_conn.read_very_eager()
    pynet_rtr1.disable_paging(remote_conn)

    output = pynet_rtr1.send_command(remote_conn, 'show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
