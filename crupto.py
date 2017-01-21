import io
import sys
import os
import string


def myxor_crypt(str):
    new_s = []
    for c in str:
        n = ord(c) ^ 2
        new_s.append(chr(n))
    nw = "".join(new_s)
    return nw

def myxor_decrypt(str):
    new_s = []
    for c in str:
        n = ord(c) ^ 2
        new_s.append(chr(n))
    nw = "".join(new_s)
    return nw


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


##allchar = string.ascii_letters + string.punctuation + string.digits
##password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
##
##password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
##
##
##addr= getMacAddress()
##addr_arr = addr.split(':')
mc_file = open("Key.dat", "wb")
addr= getMacAddress()
new_a = myxor_crypt(addr)

mc_file.write(new_a)

mc_file.close()
print new_a

abc = myxor_decrypt(new_a)
print abc

raw_input("press Any key to Exit...")
