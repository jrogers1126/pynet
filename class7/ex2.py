#!/usr/bin/env python
import pyeapi, sys, argparse, pprint
#pynet.py is in ~/pylib https://github.com/jrogers512/pynet/blob/master/pynet.py
import pynet 

def valid_id(i):
    ##Check that the VLAN is valid and not already in use
    vlan_id = int(i)
    if vlan_id > 999 or vlan_id < 100:
        raise argparse.ArgumentTypeError("Only VLAN's between 100 and 999 are allowed")
    return vlan_id

def main():
    parser = argparse.ArgumentParser("ex2.py")
    parser.add_argument('--check', action="store_true", dest="check_only", default=False, help='Do not make changes, check only')
    parser.add_argument('--remove', action="store_true", dest="remove_vlan", default=False, help='Delete the VLAN')
    parser.add_argument('--name', action="store", dest="vlan_name", help='VLAN name')
    parser.add_argument('device', action="store", help='device hostname as found in ~/.eapi.conf, see https://eos.arista.com/introducing-the-python-client-for-eapi-pyeapi/')
    parser.add_argument('vlan_id', type=valid_id, action="store", help='The VLAN ID to work with')
    args = parser.parse_args()
    try:
        args.vlan_id
    except NameError:
        args.vlan_id = 100
    try:
        args.vlan_name
    except NameError:
        args.vlan_name = 'VLAN' + str(vlan_id)
    device = pyeapi.connect_to(args.device)
    if not args.remove_vlan or args.check_only:
        if check_vlan(args.vlan_id, args.vlan_name, device):
            pass #VLAN Check is ok, go ahead and add it
            add_vlan(args.vlan_id, args.vlan_name, device)
        else:
            print "ERR: 123, this should never happen"
    else:
        remove_vlan(args.vlan_id, device)

def remove_vlan(vlan_id, device):
    cmds = ['no vlan ' + str(vlan_id)]
    if device.config(cmds):
        print "Deleting VLAN" + str(vlan_id)

def add_vlan(vlan_id, vlan_name, device):
    cmds = ['vlan ' + str(vlan_id), 'name ' + vlan_name]
    #Wouldn't mind having some error handling here, but I'm not sure what sort of 'return' from the .config method might be interpretted as an error?
    if device.config(cmds):
        print "Adding the " + vlan_name + " VLAN with ID " + str(vlan_id)

def check_vlan(vlan_id, vlan_name, device):
    vlans = device.enable("show vlan")[0]['result']['vlans']
    vlan_list = vlans.keys()
    #vlans = map(int, vlans) ##pylint says not to do this
    vlan_list = [int(i) for i in vlan_list]
    ##VLAN ID check
    if vlan_id in vlan_list:
        print >> sys.stderr, "Vlan " + str(vlan_id) + " is already in use, quitting."
        sys.exit(1)
    else:
        print "VLAN " + str(vlan_id) + " is available"
    ##VLAN Name check 
    for vlan_id, attribs in vlans.iteritems():
        if attribs['name'] == vlan_name:
            print >> sys.stderr, "VLAN Name " + vlan_name + " already in use on VLAN " + vlan_id + ", quitting."
            sys.exit(2)
    return True

if __name__ == "__main__":
    main()

