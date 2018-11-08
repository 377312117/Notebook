from socket import *
import os

os.chdir("/home/tarena")
s = socket(AF_UNIX,SOCK_STREAM)

sock_file = ("./sock3")
s.connect(sock_file)

while True:
    msg = input(">>")
    if not msg:
        break
    s.send(msg.encode())
s.close()
