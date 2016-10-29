#!/usr/bin/env python
##Import stuff
import pickle, pysnmp, snmp_helper, time, pprint

'''
    Collect snmp stats and store them in a file that will be used by excercise2-graph.py to draw an svg.  normally this would be called by some cron type thing, but in interest of focusing on the assignment only, we'll define a function that collects once, then call that once in the main() (leaving room to write some sort of 'repeat ever X minutes poller in main())
    
    Logic:
    # Read in any existing objects from the pickle jar
    # Collect input and output octets and unicast packets on interface FA4 on pynet-rtr1 every five minutes for an hour
    # save the data to a parseable file

    To run it every 5 minutes for the next hour:
    for min in {0..60..5}; do echo ./excercise2-collector.py | at now + $min minutes; done
    atq

    During this hour, optionally generate some traffic:
    while true; do sleep $( echo $(( $RANDOM/300 )) ); snmpwalk -v1 -c galileo 184.105.247.70; done

    The relevant OIDs are as follows:
'''
def main():
    #List of oid's to collect each polling
    OIDS = {
        'ifName_fa4': '.1.3.6.1.2.1.31.1.1.1.1.5',
        'ifDescr_fa4': '1.3.6.1.2.1.2.2.1.2.5',
        'ifInOctets_fa4': '1.3.6.1.2.1.2.2.1.10.5',
        'ifInUcastPkts_fa4': '1.3.6.1.2.1.2.2.1.11.5',
        'ifOutOctets_fa4': '1.3.6.1.2.1.2.2.1.16.5',
        'ifOutUcastPkts_fa4': '1.3.6.1.2.1.2.2.1.17.5',
    }
    device = ('184.105.247.70',161)
    snmp_user = ('pysnmp', 'galileo1', 'galileo1')
    device_name = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(device, snmp_user, oid='.1.3.6.1.2.1.1.5.0'))
    filename = device_name + ".fa4.pkl"
    #Read in any existing objects from the pickle jar
    try:
        f = open(filename, "rb")
        samples = pickle.load(f)
        f.close()
    except:
        samples = []
        print "Couldn't open pickle jar" 
    #Collect input and output octets and unicast packets on interface FA4 on pynet-rtr1 every
    collection = { 'timestamp': time.time() }
    for oid in OIDS:
        collection[oid] = snmp_helper.snmp_extract(snmp_helper.snmp_get_oid_v3(device, snmp_user, oid=OIDS[oid]))
    ## I'm having trouble with data structures.  It seems to me that maybe I should create a dictionary of dictionaries here?  ie, have { timestamp: sample }, where timestamp is the actual timestamp, and sample is a dictionary containing all of the OID key/value pairs?  Then I'd be able to sort the top level dictionary and pull out values of the inner one?  not sure.  I get the distinctive feeling I'm making it more complex than it needs to be, and have got it to a place whre 'it works', so I'm leaving it for now.  Suggestions are welcomed.
    samples.append(collection)
    #Write it back out to file
    with open(filename, 'wb+') as f:
        pickle.dump(samples, f) 
 
##Only run if not called by another file/program
if __name__ == "__main__":
    main()


