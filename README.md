# MicropythonGitDeploy

Library for deploying code to esp32 ( tested on pycom LoPy ).

This solution downloads code using wifi directly from GitHub using the GitHub-API.

The update is like this.
 * Remove all old files ( this means the board may be left without code if the download fails)
 * Download a list of all files and folders, recursively going through the different folders in the repo, including submodules, always main thread
 * Download and save each file

# secrets.py


You need to have the following information in a file named secrets.py
```python
ssid = 'Your SSID' #ssid for Wifi used for OTA using the release_push.py
pwa = 'WIFY-Pass' #wifi-passord used OTA using the release_push.py
#github basic authentication 

#Make token at: https://github.com/settings/tokens
#Then base64 encode "username:token" here https://www.base64encode.org/
basicAuthentication = ""
```

Example usage 

```python 
#main.py
import secrets
from network import WLAN
from gitDeploy import gitDeploy
from DeployServer import DeployServer
import time

#Connect to wifi
wlan = WLAN()
wlan.init()
wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')
print('connected')

#dont remove these files on an upload:
filesToKeep=["secrets.py"]
#dont upload these files:
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf']
#GH-username of repo and repo name
gd = gitDeploy("dntoll", "MicropythonGitDeploy", filesToKeep, ignoreUpload)

#gd.deploy() <- triggers a deploy of https://github.com/dntoll/MicropythonGitDeploy

#Start an optional web-server that initiates an deploy on "http://ip/deploy
ds = DeployServer(gd, wlan, 80)
#Get the ip
print(wlan.ifconfig()[0])