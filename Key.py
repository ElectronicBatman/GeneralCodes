import io
import sys
import os
import string
from random import *
min_char = 8
max_char = 12

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


allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))

password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))


addr= getMacAddress()
addr_arr = addr.split(':')
mc_file = open("Key.dat", "wb")

for a in addr_arr:
    password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    new_a = a + password +'\n' 
    mc_file.write(new_a)

mc_file.close()

raw_input("press Any key to Exit...")

