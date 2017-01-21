import io
import sys
import os
from Crypto.Cipher import XOR
import base64

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

def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

addr= getMacAddress()
a=encrypt('notsosecretkey', addr)
mc_file = open("key.dat", "wb")
mc_file.write(a)
mc_file.close()
print "Key is = %s" % a
raw_input("press Any key to Exit...")

