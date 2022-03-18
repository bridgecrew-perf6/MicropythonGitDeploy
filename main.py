#setup internet connection
import secrets
import machine
from network import WLAN
from HTTPClient import HTTPClient
from GitHubClient import GitHubClient
from LoPyFileSaver import LoPyFileSaver


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
fs = LoPyFileSaver(HTTPClient('raw.githubusercontent.com'))

fs.removeOldFiles()

for f in client.files:
    fs.downloadAndSave(f.clientDirectory, f.name, f.url)

machine.reset()

#c = HTTPClient('www.google.com')
#https://api.github.com/repos/dntoll/LoRaMeshLoPyConsole/contents
#contents = c.get('/')