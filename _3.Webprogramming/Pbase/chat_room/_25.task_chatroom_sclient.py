from socket import *
import os,sys

# 发送消息
    # 循环写消息
    # 将消息发送给服务器

# 发送模块
def send_msg(s,name,addr):
    while True:
        text = input(">>")
        if text == "quit":
            msg = 'Q ' + name        # 发送Q开头标志,确认退出信息
            s.sendto(msg.encode(),addr)
            sys.exit("退出聊天室")      # pid == 0时,退出的是子进程
        msg = "C %s说%s" % (name,text)
        s.sendto(msg.encode(),addr)



# 接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        # 接收服务器发来的退出标志后退出该进程
        if data.decode() == "EXIT":   # 接收到EXIT标志,退出父进程 
            sys.exit(0)     # 退出的是父进程
        print(data.decode())

# 创建套接字
def main():
    # 从命令行输入服务器地址
    if len(sys.argv) <3:
        print("argv is Error")
        return
    HOST = sys.argv[1]
    POST = int(sys.argv[2])
    ADDR = (HOST,POST)

# 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        # L作为消息标志,服务端收到该消息则自动解析判断
        msg = 'L ' + name  
        s.sendto(msg.encode(),ADDR)
        # 等待回应
        data,addr = s.recvfrom(1024)
        if data.decode() =='ok':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # 创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)       

if __name__ == "__main__":
    main()
