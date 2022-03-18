#setup internet connection
import secrets

from network import WLAN
from gitDeploy import gitDeploy



import time



wlan = WLAN()
wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')

print('connected')

gd = gitDeploy("dntoll", "micropython-git-deploy")


