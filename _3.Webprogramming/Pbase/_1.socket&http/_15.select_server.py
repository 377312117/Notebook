# 创建IO多路复用服务器
from select  import select
from socket import *

#创建套接字
s = socket(AF_INET,SOCK_STREAM)

# 绑定套接字
s.bind(("0.0.0.0",8888))

#设置端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

#监听套接字
s.listen(5)

# 创建关键字列表,一般要和while循环,关注套接字IO,收发消息
rlist = [s]
wlist = []
xlist = [s]
while True:
    # 建立select多路复用,一旦其被关注,则避免阻塞
    rs,ws,xs = select(rlist,wlist,xlist)
    # 在rlist 内部循环
    for r in rlist:
        # 一旦 r ==s:抽象为客户端与服务端建立连接
        if r == s:
            # 连接套接字,不同客户端连接是不同的套接字
            c,addr = s.accept()
            print("Connect from",addr)
            # 将每个不同的连接客户端都加入到关注列表
            rlist.append(c)
        # 如果套接字处于加入关注列表状态.一旦客户端发送消息,则服务端接收信息
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
            print("收到:",data.decode())
            # r.send("对方已收到消息".encode())
            # 如果要使用wlist,则需要主动加入wlist,一旦主动使用,wlist自动调用
            wlist.append(r)
    for w in ws:
        w.send("收到消息".encode())
        wlist.remove(w)
    for x in xs:
        x.close()
        raise
# 关闭套接字
c.close()
s.close()