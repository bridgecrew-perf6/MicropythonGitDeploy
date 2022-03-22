#setup internet connection
import secrets

from network import WLAN
from gitDeploy import gitDeploy
from DeployServer import DeployServer
import time



wlan = WLAN()
wlan.init()
wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')

print('connected')


filesToKeep=["secrets.py"]
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf']
gd = gitDeploy("dntoll", "MicropythonGitDeploy", filesToKeep, ignoreUpload)
ds = DeployServer(gd, wlan, 80)

print(wlan.ifconfig()[0])