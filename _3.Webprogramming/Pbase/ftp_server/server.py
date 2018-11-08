# 结构设计: 使用类将功能封装
# 工作步骤：先搭建网络连接
#           设计类
#           将功能函数写在类中，逐一实现并测试

# 具体功能 ： 1.搭建网络连接
#  		服务端 ： 创建fork并发服务端程序	
# 	        客户端 ： 创建套接字，进行网络连接，连接成功后                           打印命令选项界面等待输入命令
    
#             2.设计类

#             3. 查看文件列表 
#                 客户端 ： 发送请求
#                           接收服务端确认
#                           循环接收服务器发来的文件名并打印

#                 服务端： 接收请求
#                          判断可否执行反馈结果
#                          发送文件名称  
            
#             4. 下载文件
#                  客户端 ： 发送请求  G filename
#                            接收服务端确认
#                            接收文件
                 
#                  服务端 ： 接收请求
#                            判断文件是否存在，反馈结果
#                            发送文件

import os,sys
from socket import *
import time 

# 搭建网络连接,设置全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
File_Path = ("/home/tarena/AID1808_webprogramming/Pbase/ftp_sever/ftp_file/")

class FtpServer(object):
    ''' 
    该类具有三个功能,
        初始话函数将连接套接字作为参数传入,可处理多个客户端连接请求
        1.do_list() 可以处理客户端要求查看ftp服务器的请求
        2.do_getfile()可以处理客户端要求下载的请求
        3.do_putfile()可以处理客户端要求上传的请求
    '''
    def __init__(self,c):
        self.c = c
    
    def do_list(self):
        print("执行List")
        # 获取文件列表
        file_list = os.listdir(File_Path)
        if not file_list:
            self.c.send("文件库为空".encode())
            return
        else:
            self.c.send(b"OK")
            time.sleep(0.1)
        # 将文件列表拼成大字符串
        files = ''
        for file in file_list:
            if file[0] != "." and os.path.isfile(File_Path + file):
                files = files + file + "#"
        # 将拼接好的文件名字符串发送给客户端
        self.c.sendall(files.encode())

    def do_getfile(self,filename):
        '''
        下载文件功能
            逻辑顺序: 
                1.首先客户端命令行输入Get后
                2.发送由G+SPACE+文件名组成的字符串并经过编码
                3.收到信息后调用发送函数do_getfile
                4.读取需要的文件,若不存在则报错
                5.成功会收到OK,并继续执行剩余语句语句
        '''        
        print("执行getfile")
        try:
            fd = open(File_Path + filename,"rb")
        except:
            self.c.send("文件不存在".encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        #发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send(b"##")
                break
            self.c.send(data)
        print("文件发送完毕")

    def do_putfile(self,filename):
        '''逻辑与do_getlist()类似'''
        try:
            fd = open(File_Path + filename,"wb")
        except:
            self.c.send("上传失败".encode())
            return
        else:
            self.c.send(b'OK')
        while True:
            data = self.c.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()
        print("接收完毕")

# 创建网络连接
def main():
    '''创建套接字,并建立连接,实现处理客户端查看,上传,下载三个功能'''
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    # 接受连接
    while True:
        try:
            c,addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit()
        except Exception as e:
            print("服务器异常",e)
            continue
        print("连接客户端:",addr)   
        
        # 调用fork()创建子进程,
        pid = os.fork()
        if pid ==0:
            p = os.fork()  # 创建二级子进程
            if p == 0:
                ftp = FtpServer(c)
                s.close()   # 二级子进程关闭服务端套接字,为的是避免混淆.在已经连接的情况下,本身的套接字可关闭
                while True:
                    data = c.recv(1024).decode()
                    if not data or data[0] == "Q":
                        c.close()
                        sys.exit("客户端退出")
                    elif data[0] == "L":
                        ftp.do_list()
                    elif data[0] == 'G':
                        filename = data.split(" ")[-1]
                        print("发送文件:",filename)
                        ftp.do_getfile(filename)
                    elif data[0] == 'P':
                        filename = data.split(" ")[-1]
                        print("接收文件:",filename)
                        ftp.do_putfile(filename)          
            else: #一级子进程进程结束,二级子进程变为孤儿进程
                os._exit(0)
        else:
            '''os.wait()是等待父进程的任何子进程结束后才会结束'''
            c.close()
            os.wait()
# 测试函数,作为主函数则进行执行main()
if __name__ == "__main__":
    main()
