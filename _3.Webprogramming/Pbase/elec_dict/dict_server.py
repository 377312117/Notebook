'''
电子词典的服务端
功能:
    1.建立连接套接字,与客户端进行数据交互
    2.验证账户密码,并返回验证结果
    3.客户端退出时,与服务端断开连接
    4.使用多进程来处理多并发的程序请求
    5.查询单词时,在数据库调出解释
要点:
    1.不同的命令要有不同的提示符,进入不同的功能

扩展
    创建数据表
    用户表   id name ppsswd
    历史记录    id name  word  time
    单词表     id   word interpret
'''

# 调用模块
from socket import *
import time 
import sys
from os import _exit,fork,wait
from settings import *
# 调用执行pymysql语句
from python_mysql import *


# 创建python_mysql实例
sqlh = Mysqlpython("elec_dict")



class DictServer(object):
    '''负责将电子词典的服务端的功能封装在该类中
        包括了连接套接字,交互信息等功能,以及客户端功能的后台处理'''
    def __init__(self,addr):
        self.addr = ADDR
        self.port = PORT
        self.serve_socket()
    
    def serve_socket(self):
        '''建立服务器端套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.addr)
    
    def serve_forever(self):
        '''建立永久连接'''
        self.sockfd.listen(5)
        print('listen to the port %d' % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
                print('与客户端建立连接')
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit('服务端退出')
            except Exception as e:
                print('Error:',e)
                continue
            pid = fork()
            if pid == 0:
                p = fork()
                if p ==0:
                    self.sockfd.close()
                    while True:
                        data = connfd.recv(1024).decode()
                        if data[0] == 'Q' or not data:
                            connfd.close()
                            sys.exit('客户端断开连接')
                        elif data[0] == 'L':
                            print('执行登录功能')
                            user_name = data.split(' ')[-1]
                            self.do_verifylogin(connfd,user_name)
                        elif data[0] == 'R':
                            print('执行注册功能')
                            user_name = data.split(' ')[-1]
                            self.do_registeruser(connfd,user_name)
                        elif data[0] == 'C':
                            print('执行查询功能')
                            word = data.split(' ')[-2]  # 也要改变
                            user_name = data.split(' ')[-1]
                            self.do_queryword(connfd,word,user_name)
                        elif data[0] == 'S':
                            print('查询历史记录')
                            user_name = data.split(" ")[-1]
                            print(user_name)
                            self.do_selecthist(connfd,user_name)
                else:
                    _exit(0)
            else:
                connfd.close()
                wait()   # 等待子进程结束才结束父进程

    def do_queryword(self,connfd,word,user_name):
        '''负责客户端的查询功能'''
        wordphrase = sqlh.select('select * from word_phrase where word= %s;',word)
        print('查询结果为:',wordphrase)
        tm =time.ctime()
        if not wordphrase:
            print('无查询结果')
            connfd.send(b'not exist')
        else:
            print('查询到单词,返回解释')
            senddata = "OK"
            connfd.send(senddata.encode())
            time.sleep(0.1)
            senddata = wordphrase[0][2]
            connfd.send(senddata.encode())
            sqlh.zhixing('insert into hist(name,word,time) values(%s,%s,%s)',[user_name,word,tm])


    def do_verifylogin(self,connfd,user_name):
        '''负责客户端的登录功能'''
        result = sqlh.select('select * from user_info where user_name=%s',[user_name])
        if not result:
            print('无查询结果,无法登陆')
            connfd.send(b'notexist')
        else:
            print('查询到用户名,返回结果')
            senddata = 'OK'+' '+result[0][1]+' '+result[0][2]
            connfd.send(senddata.encode())
    
    def do_registeruser(self,connfd,user_name):
        '''负责客户端的注册功能'''
        result = sqlh.select('select * from user_info where user_name=%s',[user_name])
        if not result:
            print('无重复用户名,执行注册')
            connfd.send(b'OK')
            data =connfd.recv(2048).decode().split(' ')
            sqlh.zhixing('insert into user_info(user_name,password) values(%s,%s)',data)
        else:
            print('查询到已经注册,返回结果')
            connfd.send(b'already exist')
    
    def do_selecthist(self,connfd,user_name):
        '''查看查询历史记录'''
        result = sqlh.select('select * from hist where name=%s',[user_name])
        if not result:
            print('无历史记录')
            connfd.send(b'notexist')
            return
        else:
            connfd.send(b'OK')
            time.sleep(0.1)
        for i in result:
            senddata = '%s   %s   %s' %(i[1],i[2],i[3])
            connfd.send(senddata.encode())
            time.sleep(0.1)
        connfd.send(b'##')



def main():
    dict_server = DictServer(ADDR)
    dict_server.serve_forever()

if __name__ == '__main__':
    main()