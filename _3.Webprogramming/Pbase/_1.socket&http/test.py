# 使用poll创建多路复用
from select import *
from socket import *

# 创建套接字
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

# 创建poll对象,由元组组成的列表
p = poll()

# 创建查找字典
fddic = {s.fileno():s}

# 注册要关注的IO
p.register(s,POLLIN | POLLERR)

while True:
    print("等待阻塞IO")
    events = p.poll()   # 调用poll类下的实例方法
    for fd,event in events:
        if fd  == s.fileno() :
            c,addr=fddic[fd].accept()
            print("come from",addr)
            # 添加新的关注事件
            p.register(c,POLLIN | POLLHUP)
            fddic[c.fileno()] = c
        elif event & POLLIN:
            data = fddic[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fddic[fd].close()
                del fddic[fd]
            else:
                print("Recive:",data.decode())
                fddic[fd].send("收到了".encode())


