import usocket
import _thread
import time
from network import WLAN
import pycom



class DeployServer:
    def __init__(self, gd, wlan, port):
        _thread.start_new_thread(DeployServer.serverListenThread, (gd, wlan, port))
    
    def serverListenThread(gd, wlan, port):
        # Set up server socket
        serversocket = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        serversocket.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
        serversocket.bind((wlan.ifconfig()[0], 80))

        print("listening")
        # Accept maximum of 5 connections at the same time
        serversocket.listen(5)

        # Unique data to send back
        c = 1
        while True:
            # Accept the connection of the clients
            (clientsocket, address) = serversocket.accept()
            # Start a new thread to handle the client
            _thread.start_new_thread(DeployServer.client_thread, (clientsocket, c, gd))
            c = c+1
        serversocket.close()

    # Thread for handling a client
    def client_thread(clientsocket,n, gd):
        # Receive maxium of 12 bytes from the client
        r = clientsocket.recv(4096)

        # If recv() returns with 0 the other end closed the connection
        if len(r) == 0:
            clientsocket.close()
            return
        else:
            # Do something wth the received data...
            print("Received: {}".format(str(r))) #uncomment this line to view the HTTP request

        http = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection:close \r\n\r\n" #HTTP response
        
        if "GET / " in str(r):
            #this is a get response for the page   
            # Sends back some data
            clientsocket.send(http + "Go deploy!")
        elif "GET /deploy "in str(r):
            clientsocket.send(http + "Deploy!")
            gd.deploy()
            
       
        # Close the socket and terminate the thread

        clientsocket.close()



