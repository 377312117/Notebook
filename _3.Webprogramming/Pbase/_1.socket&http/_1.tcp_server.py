from socket import *

# 创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

# 设置绑定地址
sockfd.bind(("127.0.0.1",8888))

# 设置监听
sockfd.listen(5)

# 
# 接受客户端的连接
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)   # 打印客户端地址

# 收发消息
while True:
    data = connfd.recv(1024)   # receive 也是阻塞函数
    if data == "连接结束".encode():
        print("客户端请求断开,连接结束")
        connfd.close()
        sockfd.close()
        break
    else:
        print("接受消息为>>",data.decode())
        data1 =  input("需要返回的信息为>>")
        connfd.send(data1.encode())    # 或者是用encode方法
        print("消息已发送")
# 关闭套接字
