# 使用tcp完成一个文件的传输,要求可以传输文本文件和图片文件,从客户端发送给服务端,或者从
# 服务端发送给客户端均可
from socket import *
import os

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)
sockfd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 绑定地址
sockfd.bind(("0.0.0.0",8888))

# 设置监听
sockfd.listen(5)

# 等待客户端连接请求
print("等待连接...")
confd,addr = sockfd.accept()
print("连接地址是",addr)

# 收发
os.chdir("/home/tarena")
s1 = input("请输入下载文件名")
f = open(s1,"wb")
print("打开文件成功")
while True:
    data = confd.recv(1024)
    if not data:
        print("服务端请求断开连接,连接结束")
        break
    f.write(data)
print("写入成功")

# data1 = input("需要返回的信息为:")
# confd.send(data1.encode())

#关闭连接
f.close()
confd.close()
sockfd.close()