from socket import * 

s = socket()
# 设置端口可以立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 套接字地址族
print(s.family)

# 套接字类型
print(s.type)

# 获取套接字绑定地址
s.bind(("176.140.4.195",8888))
print(s.getsockname())

# 获取文件描述符
print(s.fileno())

s.listen(3)

c,addr = s.accept()

# 客户端链接套接字获取对应客户端地址
print(c.getpeername())