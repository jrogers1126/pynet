import passwords

rtr1 = {
    'hostname': '184.105.247.70',
    'username': 'pyclass',
    'device_type': 'ios',
    'password': passwords.passwords[0],
    'merge_file': 'ex2_rtr1.conf'
}
rtr2 = {
    'hostname': '184.105.247.71',
    'username': 'pyclass',
    'device_type': 'ios',
    'password': passwords.passwords[0],
}
sw1 = {
    'hostname': '184.105.247.72',
    'username': 'admin1',
    'device_type': 'eos',
    'password': passwords.passwords[1]
}
sw2 = {
    'hostname': '184.105.247.73',
    'username': 'admin1',
    'device_type': 'eos',
    'password': passwords.passwords[1]
}
srx1 = {
    'hostname': '184.105.247.76',
    'username': 'pyclass',
    'device_type': 'junos',
    'password': passwords.passwords[0]
}
srx2 = {
    'hostname': '127.0.0.1',
    'username': 'pyclass',
    'device_type': 'junos',
    'password': passwords.passwords[0],
    'optional_args': {
        'port': 2222
    }
}

