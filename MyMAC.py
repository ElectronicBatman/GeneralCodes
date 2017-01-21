import io
import sys
import os
import msvcrt as m

def getMacAddress(): 
    if sys.platform == 'win32': 
        for line in os.popen("ipconfig /all"): 
            if line.lstrip().startswith('Physical Address'): 
                mac = line.split(':')[1].strip().replace('-',':') 
                break 
    else: 
        for line in os.popen("/sbin/ifconfig"): 
            if line.find('Ether') > -1: 
                mac = line.split()[4] 
                break 
    return mac


def wait():
    m.getch()

addr= getMacAddress()
print "MAC Address is = %s" % addr
raw_input("press Any key to Exit...")

