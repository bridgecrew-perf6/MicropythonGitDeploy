#setup internet connection
import secrets
from network import WLAN
from HTTPClient import HTTPClient
from GitHubClient import GitHubClient

import time



wlan = WLAN()
wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')

print('connected')



#https://api.github.com/repos/dntoll/LoRaMeshLoPyConsole/contents
c = HTTPClient('api.github.com')
client = GitHubClient(c, "dntoll", "LoRaMeshLoPyConsole")

for f in client.files:
    print(f)
    

#c = HTTPClient('www.google.com')
#https://api.github.com/repos/dntoll/LoRaMeshLoPyConsole/contents
#contents = c.get('/')