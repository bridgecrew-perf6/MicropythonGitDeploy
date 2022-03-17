import socket
import ssl
import time

class HTTPClient:
    def __init__(self, host):
        # setup socket for connection
        s = socket.socket()
        self.s = ssl.wrap_socket(s)
        self.host = host
        addr = socket.getaddrinfo(self.host,443)[0][-1]
        self.s.connect(addr)
        self.s.setblocking(True)
        self.s.settimeout(1)
        print('socket connected')
    
    def get(self, url):
        # it is possible to attach additional HTTP headers in the line below, but note to always close with \r\n\r\n
        httpreq = 'GET '+url+' HTTP/1.1\r\nHOST: '+ self.host + '\r\nUser-Agent: pycomer\r\nCache-Control: no-cache\r\n\r\n'
        print('http request: \n', httpreq)
        self.s.send(httpreq)


        maxBytes = 1370

        try:
            rec_bytes = self.s.recv(maxBytes)
            buffer = rec_bytes

            while len(rec_bytes) != 0:
                
                rec_bytes = self.s.recv(maxBytes)
                buffer = buffer + rec_bytes
        except:
            print("crap")
        return bytes(buffer)

    def close(self):
        self.s.close()
