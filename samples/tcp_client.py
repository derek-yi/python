#!/usr/bin/evn python

from socket import *

HOST='127.0.0.1'
PORT=1024
BUFFSIZE=512
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    print("send data:", data)
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFFSIZE).decode()
    if not data:
        break
    print("recv data:", data)

tcpCliSock.close()
    
