import os,sys
from socket import *
import time
from threading import Thread

# 搭建网络连接,设置全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

def handler(c):
    print("Connect from",c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.dacode())
        c.send(b'Receive')
    c.close()

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)


while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit()
    except Exception as e:
        print(e)
        continue
    # 创建线程 
    t = Thread(target=handler,args = (c,))
    t.setDaemon(True)
    t.start()