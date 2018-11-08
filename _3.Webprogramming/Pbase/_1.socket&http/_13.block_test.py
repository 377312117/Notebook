from socket import *
from time import sleep,ctime

# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)


# 设置非阻塞状态
sockfd.setblocking(False)
# 设置超时时间
# sockfd.settimeout(5)


while True:
    print("Waiting for connect")
    try:
        connfd,addr = sockfd.accept()
        # 捕获非阻塞异常
    except BlockingIOError:
        sleep(2)
    # except timeout:
    #     print(ctime())
        # continue
    else:
        print("Connect from",addr)
        data = connfd.recv(1024)
        print("Receive:",data)
        connfd.close()
sockfd.close()
