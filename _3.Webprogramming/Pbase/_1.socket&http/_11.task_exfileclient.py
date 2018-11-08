# 创建客户端
from socket import * 
import os

# 创建套接字
confd = socket()
confd.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 发起连接
server_addr = ("127.0.0.1",8888)
confd.connect(server_addr)

# 收发消息
os.chdir("/home/tarena")
s1 = input("请输入传输文件名")
f1 = open(s1,"rb")
print("成功打开文件")
while True:
    recvf = f1.read(1024)         
    if not recvf: 
        print("读取完毕")
        break      
    confd.send(recvf)     

# s2 = input ("请输入下载文件名")
# f2 = open(s2,"wb")   # 打开文件,用f绑定文件流对象
# while True:
#     data1 = confd.recv(1024)
#     if not data1:
#         break
#     f2.write(data1)

# 连接结束
f1.close()
confd.close()