# 作业:
#     对进程的要求的理论进行总结
#     整理网络编程知识点,回顾重点程序
#     聊天室
#         要求
#             类似与qq群聊,
#         功能
#             每个人进入聊天室的时候其他人会受到通知
#                xxx 进入的聊天室
#             每个人退出也会给其他人通知
#                xxx 退出了聊天室
#             进入聊天室 需要输入姓名,姓名不能和已有的重复
#             进入聊天室一人发言其他人都能收到
#                xxx   说:  xxxxxxx
#             管理员喊话群里都能收到:
#                管理员 说:  xxxxxxx

# 确认技术模型
#     如何将客户端的信息发给所有人能看到
#         利用服务端转发,服务器接收,然后转发给其他人
#     用哪种服务器
#         udp,因为简单很多
#     用户存储
#         要存姓名地址,采用字典{name:ip}
#     发送和接收互不干扰
#         发送和接收用不同的进程分别处理发送接收,多进程

# 整体设计
#     封装
#         将每个功能封装成函数
#     测试
#         实现一个功能,测试一个功能
#     编写流程
#         搭建网络连接,然后进行逐个功能的实现
#     细化流程,
#         建立流程图,将需要的功能有条不紊的实现

# 登录
    # 服务端
        # 接收姓名
        # 判断姓名是否存在
        # 根据判断结果返回相应的信息
        # 如果不允许登录则功能结束
        # 如果允许登录将用户加入维护的数据结构
        # 将用户登录提示信息发送给其他人

    # 客户端
        # 输入姓名
        # 发送姓名给服务端,进行登录名比对
        # 接收服务端确认信息
        # 如果不允许则重新输入
        # 如果允许则进入聊天室
        # 创建新的进程,一个用于收消息,一个用于发消息

# # 发送消息
    # 服务端
        # 受到消息判定请求类型
        # 调用函数处理:将消息转发给其他人
# 管理员发言

# 退出
    # 服务端
        # 接收消息确定消息类型
        # 将用户从字典移除
        # 给其他人发送通知
        # 给退出的客户端发送标志

    # 客户端
        # 当输入quit表示退出,发送退出消息给客户端,客户端进程退出
        # 接收特殊标志退出进程

# 导入模块
from socket import *
import os,sys


# 发送模块
def do_send(s,user,name,msg):
    msg = "%s  %s"  % (name,msg)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

# 退出模块
def do_quit(s,user,name):
    msg = "\n%s 退出了聊天室" % name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])    # 发送EXIT标志,对面接收到终止父进程
            sys.exit(0)
        else:
            s.sendto(msg.encode(),user[i])
    # 从字典删除用户
    del user[name]

# 进行登录名判断
def do_login(s,user,name,addr):
    if (name in user) or name =="管理员":
        s.sendto("该用户已存在".encode(),addr)
        return 
    s.sendto(b'ok',addr)
    # 通知其他人
    msg = "欢迎 %s 进入聊天室" % name
    print(msg)
    for i in user:
        s.sendto(msg.encode(),user[i])
    # 将用户加入user
    user[name] = addr

def do_request(s):
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        # 将获得的字符串进行切割
        msgList = msg.decode().split(" ")
        # 区分请求类型
        if msgList[0] == "L":
            # 进行登录名判断,理清所需要的参数
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == "C":
            # C开头的为聊天内容
            msg = ' '.join(msgList[2:])
            do_send(s,user,msgList[1],msg)
            # print(msg,addr)
        elif msgList[0] == "Q":
            # 接收数据标志Q开头的数据为退出,调用do_quit函数
            do_quit(s,user,msgList[1])
            

# 网络连接
    # 服务端:创建套接字,绑定地址
    # 客户端:创建套接字
'''Note: Chatroom  env: Python 3.5 sock and fork'''
# 创建网络连接
def main():
    '''创建数据报套接字,提供客户端连接借口'''
    s = socket(AF_INET,SOCK_DGRAM)
    # 建立连接地址
    server_addr = ("0.0.0.0",8899)
    # 设置端口可重用
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定地址
    s.bind(server_addr)

# 创建子进程
    pid = os.fork()
    if pid < 0:
        print("创建进程失败")
        return
    elif pid == 0:  
        # 子进程负责发送管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员" + msg
            s.sendto(msg.encode(),server_addr)
    else:
    # 父进程用于接收各种服务端请求,调用相应的函数处理
        do_request(s)          # 调用108行do_request函数

if __name__ == "__main__":
    main()

# # 关闭套接字
# socket.close()

