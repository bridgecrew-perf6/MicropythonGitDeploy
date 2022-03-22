import socket
import ssl
import time
import ubinascii


class HTTPResponse:
    def __init__(self, responseBytes):
        header, self.body = responseBytes.decode("utf-8").split("\r\n\r\n", 1)
        self.headers = header.split("\r\n")
    def failed(self):

        if self.headers[0].endswith("200 OK"):
            return False
        return True

    def needsAuthentication(self):

        if self.headers[0].endswith("401 Unauthorized"):
            return True
        return False


class HTTPClient:
    def __init__(self, host, accessToken):
        # setup socket for connection
        s = socket.socket()
        self.s = ssl.wrap_socket(s)
        self.host = host
        addr = socket.getaddrinfo(self.host,443)[0][-1]
        self.s.connect(addr)
        self.s.setblocking(True)
        self.s.settimeout(0.5)
        self.accessToken = accessToken
        #print('socket connected')
    
    def get(self, url):
        # it is possible to attach additional HTTP headers in the line below, but note to always close with \r\n\r\n
        authentication = "\r\nAuthorization: Basic " + self.accessToken
        httpreq = 'GET '+url+' HTTP/1.1\r\nHOST: '+ self.host + '\r\nUser-Agent: pycomer\r\nCache-Control: no-cache' + authentication + '\r\n\r\n'
        #print('http request: \n', httpreq)
        self.s.send(httpreq)


        maxBytes = 10000

        buffer = b""

        try:
            rec_bytes = self.s.recv(maxBytes)
            buffer = rec_bytes
            print("Received: " + str(len(rec_bytes)))

            while len(rec_bytes) != 0:
                rec_bytes = self.s.recv(maxBytes)
                #print("Received: " + str(len(rec_bytes)))
                buffer = buffer + rec_bytes
        except:
            #print("crap")
            pass
        return HTTPResponse(bytes(buffer))

    def close(self):
        self.s.close()
