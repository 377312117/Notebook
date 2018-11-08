from socket import *
from select import *

# 创建关注的io
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(5)

# 创建poll对象
p = epoll()

# 建立查找字典
fdmap = {s.fileno():s}

# 注册要关注的IO
p.register(s,EPOLLIN | EPOLLERR)

# 监控要关注的IO
while True:
    print("阻塞等待IO")
    events = p.poll()
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的关注事件
            p.register(c,EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send("收到了".encode())