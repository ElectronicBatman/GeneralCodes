import time
import os
from time import ctime
try:
    import ntplib
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    print response.tx_time
    newtime = ctime(response.tx_time)
    print newtime
    #datetime.datetime.utcfromtimestamp(x.request('europe.pool.ntp.org').tx_time)
    #os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
    print('Could not sync with time server.')

print('Done.')
