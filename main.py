import pycom
import machine
pycom.pybytes_on_boot(True)


from gitdeploy.HTTPClient import HTTPClient


hc = HTTPClient("LNU-iot", "modermodemet")