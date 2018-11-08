# 此测试文件复原了ftp服务器的简单搭建
# 1.分析需求
    # 实现3个功能,查看文件,下载文件,上传文件
    # 可以的话尝试将创建套接字,连接套接字也封装在类中
# 2.技术难点
    # 搭建类,
    # 服务器的搭建
    # 不同功能的首字符作为区分
    # 创建多进程将收发进程进行合理分割
# 3.具体实现
    # 导入模块.创建类
    # 划分功能
    # 主函数

from socket import *
from time import sleep
import os,sys

class FTPServer(object):
    def __init__(self,server_addr,ftp_dir):
        self.server_addr = server_addr
        self.ftp_dir = ftp_dir
        self.id = server_addr[0]
        self.port =server_addr[1]
        self.get_socket()

    def get_socket(self):
        '''建立服务器端的套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)
        
    def serve_forever(self):
        '''建立永久连接'''
        self.sockfd.listen(5)
        print("Listen to the port %d" % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
                print("与客户端建立连接!")
            except KeyboardInterrupt:
                self.sockfd.close()
                print("服务器端退出!")
                sys.exit(0)
            except Exception as e:
                print("Error:",e)
                continue
            pid = os.fork()
            if pid == 0:  # 子进程进行具体发送的功能
                p = os.fork()
                if p == 0:
                    self.sockfd.close()
                    while True:
                        data = connfd.recv(1024).decode()
                        if not data or data[0] == 'Q':
                            connfd.close()
                            sys.exit("客户端断开连接")
                        if data[0] == 'L':
                            self.do_list(connfd)
                        elif data[0] == 'G':
                            filename = data.split(" ")[-1]
                            print("发送文件")
                            self.get_file(connfd,filename)
                        elif data[0] == "P":
                            filename = data.split(" ")[-1]
                            self.put_file(connfd,filename)
                else:
                    os._exit(0)
            else:
                connfd.close()
                os.wait()   # 等子进程结束才结束父进程

    def do_list(self,connfd):
        print("查看文件列表")
        file_list = os.listdir(self.ftp_dir)
        if not file_list:
            connfd.send("文件夹为空!".encode())
            return
        else:
            connfd.send("OK".encode())
            sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != "."  or os.path.isfile(ftp_dir + file):
                files = files + file + "#"
        connfd.sendall(files.encode())

    def get_file(self,connfd,filename):
        print("执行下载程序")
        try:
            fd = open(self.ftp_dir + filename,"rb")
        except:
            connfd.send("文件不存在".encode())
            return
        else:
            connfd.send(b"OK")
            sleep(0.1)
        while True:
            data1 = fd.read(1024)
            if not data1:
                sleep(0.1)
                connfd.send(b'##')
                fd.close()
                break
            connfd.send(data1)
        print("文件发送完毕")
    
    def put_file(self,connfd,filename):
        print("执行上传程序")
        try:
            fr = open(self.ftp_dir + filename,'wb')
        except:
            connfd.send("客户端上传失败!".encode())
            return
        else:
            connfd.send(b'OK')
        while True:
            data2 = connfd.recv(1024)
            if data2 == b"##":
                break
            fr.write(data2)
        print("上传成功")

    

def main():
    server_addr = ("0.0.0.0",8800)
    ftp_dir = ("/Users/zhaozhengxing/Documents/OneDrive/python3/AID1808_webprogramming/Pbase/ftp_server/ftp_file/")
    ftp_server = FTPServer(server_addr,ftp_dir)
    ftp_server.serve_forever()

if __name__  ==  "__main__":
    main()