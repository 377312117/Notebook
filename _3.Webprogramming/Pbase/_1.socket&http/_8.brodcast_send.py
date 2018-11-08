from socket import *
from time import sleep

# 目标地址
dest = ('176.140.4.255',3333)

s = socket(AF_INET,SOCK_DGRAM)

# 设置可以发送接收广播,设置端口重用
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    i = 1
    while i <= 100:
        sleep(2) 
        s.sendto(str(i).encode(),dest)
        i+=1
s.close()

