import datetime
import ntplib
from _winreg import *
from time import ctime
print r"*** Reading from SOFTWARE\Microsoft\Windows\CurrentVersion\Run ***"
         
keyVal = r'Software\eArtisan\ebat\Main'
try:
    key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
except:
    key = CreateKey(HKEY_CURRENT_USER, keyVal)


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
SetValueEx(key, "DATE", 0, REG_SZ, my_date)
#SetValueEx(key, "Installed", 0, REG_SZ, "1")
result = QueryValueEx(key, "DATE")
print "##############"
print result
print "###############"
CloseKey(key)
