#setup internet connection
from network import WLAN
import time
import socket
import ssl



class HTTPClient:
    def __init__(self, ssid, pwrd):
        wlan = WLAN()
        nets = wlan.scan()
        wlan.connect(ssid=ssid, auth=(WLAN.WPA2, pwrd))
        print('connecting..',end='')
        while not wlan.isconnected():
            time.sleep(1)
            print('.',end='')
        print('connected')
        # setup socket for connection
        s = socket.socket()
        s = ssl.wrap_socket(s)
        host = 'familjentoll.se'
        addr = socket.getaddrinfo(host,443)[0][-1]
        s.connect(addr)
        print('socket connected')
        httpreq = 'GET / HTTP/1.1 \r\nHOST: '+ host + '\r\nConnection: close \r\n\r\n'
        print('http request: \n', httpreq)
        s.send(httpreq)
        time.sleep(1)
        rec_bytes = s.recv(10000)
        print(rec_bytes)
        print('end')