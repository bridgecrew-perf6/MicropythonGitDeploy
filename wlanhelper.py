from network import WLAN
import time
import secrets


def wlanhelper():
    wlan = WLAN()
    wlan.init()
    wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
    print('connecting..',end='')
    while not wlan.isconnected():
        time.sleep(1)
        print('.',end='')

    print('connected')
    time.sleep(2)
    return wlan