import pycom
import network 
from network import WLAN
import machine
import time
import secrets

pycom.pybytes_on_boot(False)
pycom.smart_config_on_boot(False)
pycom.wifi_on_boot(True)
pycom.wifi_mode_on_boot(WLAN.STA)
pycom.wifi_ssid_sta(secrets.ssid)
pycom.wifi_pwd_sta(secrets.pwa)
wlan = network.WLAN(mode=network.WLAN.STA)
print(wlan.ifconfig())


