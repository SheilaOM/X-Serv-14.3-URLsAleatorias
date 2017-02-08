#!/usr/bin/python

"""
Seila Oliva Muñoz
"""

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

while True:
    a = random.randint(0, 1000000000)
    dir = "http://localhost:1234/" + str(a)

    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                          "<html><body><h1>Hola. " +
                          "<a href={}>Dame otra".format(dir) +
                          "</h1></body></html>" +
                          "\r\n", "utf-8"))
    recvSocket.close()
