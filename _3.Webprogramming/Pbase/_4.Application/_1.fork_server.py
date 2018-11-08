from socket import *
import os,sys

def client_handler(c):
    '''客户端处理函数'''
    print("客户端:",c.getpeername())   # 打印客户端的地址
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'Recevie your message')
    c.close()
    sys.exit()

# 创建套接字
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

s =socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 循环等待客户端的连接
print("listen to the port 8888...")
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("Error:",e)
        continue
    # 创建新的进程处理客户端请求
    pid = os.fork()

    # 子进程处理客户端请求
    if pid == 0:
        p = os.fork()  # 创建二级子进程处理僵尸进程
        if p == 0:
            s.close()
            client_handler(c)   # 客户端处理函数
        else:
            os._exit(0)
    # 父进程或者创建进程失败都继续等待下个客户端连接
    else:
        c.close()
        os.wait()   # 等待回收一级子进程
        continue
    