from socket import *

# 创建套接字
sockfd = socket()

# 发起连接
server_addr = ("127.0.0.1",8888)
sockfd.connect(server_addr)

# 发收消息
while True:
    data = input("需要发送的信息为:")
    if data == "":
        sockfd.send("连接结束".encode())
        print("连接结束")
        sockfd.close()
        break
    else:
        sockfd.send(data.encode())
        print("已发送")
        data = sockfd.recv(1024)
        print("接收消息为:",data.decode())
#关闭客户端
