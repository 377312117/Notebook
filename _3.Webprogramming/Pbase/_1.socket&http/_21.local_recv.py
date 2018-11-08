from socket import *
import os

os.chdir("/home/tarena")

# 确定套接字文件
sock_file = "./sock3"
s = socket(AF_UNIX,SOCK_STREAM)
s.bind(sock_file)
s.listen(3)

while True:
    c,addr = s.accept()
    while True:
        data = c.recv(1024)
        if not data :
            break
        print(data.decode())
    c.close()
    # data = s.send()
s.close()