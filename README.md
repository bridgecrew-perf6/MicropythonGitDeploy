# MicropythonGitDeploy

Library for deploying code to esp32 ( tested on pycom LoPy ).

This solution downloads code using wifi directly from GitHub using the GitHub-API.

The update is like this.
 * Remove all old files ( this means the board may be left without code if the download fails)
 * Download a list of all files and folders, recursively going through the different folders in the repo, including submodules, always main thread
 * Download and save each file


## Todo:

 * Version check ( dont update if same version )
 * Display HTTP errors 
 * Initiate Deploy in other ways (like LoRaMesh message etc)
 * Rename, download, restore on fail update mechanism
 * Error messages for common errors


## Example usage 

Place the code of this repo in your (can be submodule)

## secrets.py
You need to have the following information in a file named secrets.py
```python
ssid = 'Your SSID' #ssid for Wifi used for OTA using the release_push.py
pwa = 'WIFY-Pass' #wifi-passord used OTA using the release_push.py
#github basic authentication 

#Make token at: https://github.com/settings/tokens
#Then base64 encode "username:token" here https://www.base64encode.org/
basicAuthentication = ""
```


```python 
#setup internet connection
import secrets
from gitDeploy import gitDeploy
from DeployServer import DeployServer
from wlanhelper import wlanhelper

filesToKeep=["secrets.py"]
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf']
gd = gitDeploy("dntoll", "MicropythonGitDeploy", filesToKeep, ignoreUpload)

wlan = wlanhelper()
ds = DeployServer(gd, wlan, 80)

print(wlan.ifconfig()[0])