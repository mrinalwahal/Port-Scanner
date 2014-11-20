# !/usr/bin/env python
# Programmer - Mrinal Wahal
# Class - XI - A
# Project - Portscanner

import socket
import subprocess
import sys
from datetime import datetime
import getpass
print "-" * 60
print "       Welcome to DynaScan"
print "-" * 60
print

password = getpass.getpass("Enter your Clearance Password: ")
answer = "scanify"
if password == answer:
    portrange = "0,1204"
    print
    print "-" * 60
    remoteServer    = raw_input("Enter a remote host to scan: ")       # Ask for input
    print "-" * 60
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print "NOTE - Maxximum Port Range Cannot Exceed 1024."
    print
    u = int(raw_input("Enter Starting Port: "))
    v = int(raw_input("Enter Ending Port: "))
    print "-" * 60                                                    # info on which host to scan
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60
    print
    t1 = datetime.now()                                                # Check what time the scan started
    print "Scan Started at... ", t1

    try:
        for port in range(u,v):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                sock.close()

            print "Port {}: \t Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    t2 = datetime.now()                     # Checking the time again
    total =  t2 - t1                        # Calculates the difference of time, to see how long it took to run the script

    print 'Scanning Completed in: ', total
    print
    close = raw_input("Press any key to terminate...")
else:
    print "Clearance Not Found."
    xlo= raw_input("Press Enter To Terminate...")
    exit()

