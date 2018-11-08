from socket import *
import os,sys
import time

# 将具体功能实现放在类中
class FtpClient(object):
    ''' 将各项功能函数放在下列函数中'''
    def __init__(self,s):
        '''将套接字作为参数传入类中'''
        self.s = s

    def do_list(self):
        '''获取ftp文件列表'''
        # 发送请求
        self.s.send(b'L') 
        # 等待回复
        data = self.s.recv(128).decode()
        if data == "OK":
            data = self.s.recv(4096).decode()
            # 将接收的大字符串进行切割,分隔符为#号
            files = data.split("#")
            # 展示文件内容   
            for file in files:
                print(file)
            print("文件列表展示完毕") 
        else:
            # 无法执行操作
            print(data)

    def do_getfile(self,filename):
        '''
        下载文件功能
            逻辑顺序: 
            1.首先命令行输入Get后调用本函数
            2.发送由G+SPACE+文件名组成的字符串并经过编码
            3.对面收到信息后调用发送函数do_getfile
            4.读取需要的文件,若不存在则报错
            5.成功会收到OK,并继续执行剩余语句语句
        '''
        self.s.send(("G " + filename).encode())
        data = self.s.recv(128).decode()
        if data == "OK":
            # 确认文件存在,则继续读取并存储内容
            fd = open(filename,"wb")
            # 通过循环获得内容
            while True:
                data = self.s.recv(1024)
                # 一旦收到命令提示符##,则跳出本次循环
                if data == b"##":
                    break
                fd.write(data)
            fd.close()
            print("%s 下载完毕" % filename)
        else:
            # 如果收到的不是OK则代表下载失败,打印"文件不存在"
            print(data)

    def do_putfile(self,filename):
        '''上传文件功能,逻辑与do_getfile()类似,不过是收发功能相反'''
        self.s.send(("P " + filename).encode())
        data = self.s.recv(128).decode()
        if data == "OK":
            fd = open(filename,"rb")
            while True:
                data = fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b"##")
                    break
                self.s.send(data)
            print("文件发送完毕")
    def do_quit(self):
        '''退出客户端'''
        self.s.send(b"Q")
        self.s.close()
        sys.exit("谢谢使用")

#网络连接
def main():
    '''主程序,实现主要有三个功能:
        1.查看ftp文件夹,调用函数do_list()
        2.下载文件.调用函数do_getfile()
        3.上传文件,调用函数do_putfile()'''

    # 在命令行输入连接地址和端口号
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    #  尝试连接,连接失败则报错
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print("连接服务器失败",e)
        return

    # 创建对象,将套接字作为初始化命令传入类中,避免重复给值
    ftp = FtpClient(s)

    # 创建终端的简单可视化界面,可扩展到GUI程序上
    while True:
        print("======== Command Choice ==========")
        print("============ List ================")
        print("========== Get File ==============")
        print("========== Put File ==============")
        print("============ Quit ================")
        print("==================================\n")

        # 通过终端输出语句命令来尝试不同选项
        cmd = input("请输入命令==>>")
        # 命令List 调用 FtpClient类的do_list()函数
        if cmd.strip() == "List":
            ftp.do_list()
        # 命令Get 调用 FtpClient类的do_getfile()函数 
        elif cmd[:3] == "Get":
            filename = cmd.split(" ")[-1]   # 将文件名最后一个元素传递
            print("下载文件:",filename)
            ftp.do_getfile(filename)
        # 命令Put 调用 FtpClient类的do_putfile()函数    
        elif cmd[:3] == "Put":
            filename = cmd.split(" ")[-1]   # 将命令行最后一个元素作为文件名传递
            print("上传文件:",filename)
            ftp.do_putfile(filename)
        # 命令Quit 调用 FtpClient类的do_quit()函数      
        elif cmd.strip() == "Quit":
            ftp.do_quit()
        # 输入其他命令则继续循环
        else:
            continue

# 测试命令,本模块作为主程序则执行
if __name__ == "__main__":
    main()
