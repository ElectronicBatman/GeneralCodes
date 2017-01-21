import datetime
import ntplib
from Crypto.Cipher import XOR
import base64

from _winreg import *
from time import ctime
print r"*** Reading from SOFTWARE\Microsoft\Windows\CurrentVersion\Run ***"
def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))


def myxor_crypt(str):
    new_s = []
    for c in str:
        n = ord(c) ^ 89
        new_s.append(chr(n))
    nw = "".join(new_s)
    return nw

def myxor_decrypt(str):
    new_s = []
    for c in str:
        n = ord(c) ^ 89
        new_s.append(chr(n))
    nw = "".join(new_s)
    return nw


#keyVal = r'Software\eArtisan\ebat\Main'
keyVal = r'SOFTWARE\eArtisan\ebat\Main'
try:
    #key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
except:
    #key = CreateKey(HKEY_CURRENT_USER, keyVal)
    key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)


client = ntplib.NTPClient()
response = client.request('pool.ntp.org')
newtime = ctime(response.tx_time)
print newtime


now = datetime.datetime.now()
print str(now)
my_date = []
my_date.append(str(now.month))
my_date.append(str(now.year))
my_date = '-'.join(my_date)
print my_date
mac = '4C:72:B9:21:06:B7'
#a=encrypt('notsosecretkey', mac)
a = myxor_crypt(mac)
#print a
b=myxor_decrypt(a)
#print b
SetValueEx(key, "DATE", 0, REG_SZ, my_date)
SetValueEx(key, "APPKEY", 0, REG_SZ, a)
#SetValueEx(key, "Installed", 0, REG_SZ, "1")
result = QueryValueEx(key, "DATE")
result1 = QueryValueEx(key, "APPKEY")
print "##############"
print result
print result1[0]
b1=myxor_decrypt(result1[0])
print b1
if(b1==mac):
  print "DECR SUCCESS"
print "###############"
CloseKey(key)
