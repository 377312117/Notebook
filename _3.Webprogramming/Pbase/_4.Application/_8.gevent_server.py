# 此示例示意协程gevent和monkey的用法
import gevent
from gevent import monkey
# 执行脚本插件修改阻塞行为
monkey.patch_all()  
from socket import *

# 创建套接字
def server():
    s = socket()
    s.bind(("0.0.0.0",8888))
    s.listen(5)
    while True:
        c,addr = s.accept()
        print("Come from",addr)
        # handle(c)   # 循环方案
        gevent.spawn(handle,c)  # 协程方案

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(b'Receive message')
    c.close()
server()
