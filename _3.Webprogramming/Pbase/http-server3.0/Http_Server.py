# coding = utf-8
'''
aid httpserver v3.0
'''

from socket import *
import sys
from threading import Thread
# 导入配置文件
from settings import *
import re
import time

def connect_frame(METHOD,PATH_INFO):
    '''连接到frame服务器'''
    s = socket()
    # 连接框架服务器地址
    try:
        s.connect(frame_address) # 连接套接字
    except Exception as e:
        print('Error',e)
        return
    s.send(METHOD.encode())
    time.sleep(0.1)
    s.send(PATH_INFO.encode())
    response = s.recv(4096)
    s.close()
    return response



# 使用类封装httpserver类
class HTTPServer(object):
    '''
    包括了服务器的响应,连接,反馈数据给frame数据库等功能
    '''
    def __init__(self,address):
        '''初始定义方法'''
        self.address = address
        self.create_socket()
        self.bind(address)
    
    def create_socket(self):
        '''创建套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self,address):
        '''绑定套接字'''
        self.ip = ADDR[0]
        self.port = ADDR[1]
        self.sockfd.bind(address)

    def serve_forever(self):
        '''建立连接服务'''
        self.sockfd.listen(5)
        print('listen to the port %d' % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
                print('Connect from:',addr)
            except KeyboardInterrupt:
                print('退出连接')
                sys.exit('程序退出')
            except Exception as e:
                print('连接失败!出现错误:',e)
                continue
            clientThread = Thread(target=self.handle,args = (connfd,)) 
            clientThread.setDaemon(True)
            clientThread.start()

    def handle(self,connfd):
        '''负责对客户端发回来的信息进行解析'''
        request = connfd.recv(4096)
        if not request:
            return
        request_lines = request.splitlines()
        # 获取请求行
        request_line = request_lines[0].decode()
        # 利用正则表达式进行解析
        pattern = r'(?P<METHOD>[A-Z]+)\s+(?P<PATH_INFO>/\S*)'
        try:
            env = re.match(pattern,request_line).groupdict() #  生成字典
            print(env)  # 是一个字典{'METHOD': 'GET', 'PATH_INFO': '/'}
        except:
            response_headlers = 'HTTP/1.1 500 SERVER ERROR'
            response_headlers = '\r\n'
            response_body = 'Server Error'
            response = response_headlers + response_body
            connfd.send(response.encode())
            connfd.close()
            return
        response = connect_frame(**env)
        connfd.send(response)
    
    def send_data(self,connfd):
        '''负责将frame服务器返回的数据返回给浏览器'''
        data = connect_frame(pageframe)
        connfd.send(data.encode())
        

if __name__ == '__main__':
    httpd = HTTPServer(ADDR)
    # 启动服务器
    httpd.serve_forever()

