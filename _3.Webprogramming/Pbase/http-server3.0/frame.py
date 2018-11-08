import time
# coding =utf-8
'''
模拟框架程序部分
'''

# 应用类,将功能封装在类中

from socket import *
from threading import Thread
import sys

# 全局变量,两个服务器不能用一个settings
frameserver_ip = '127.0.0.1'
frame_port = 8080
frameserver_addr =(frameserver_ip,frame_port)
# 静态网页位置
static_dir = './static'

class Web_Frame(): 
    '''该服务器用来解析HTTPServer发送过来的需求,解析并返回网页''' 
    def __init__(self,frameserver_addr,static_dir):
        self.pape = static_dir
        self.frame_socket()
    
    def frame_socket(self):
        '''建立套接字'''
        self.frame_sockfd = socket()
        self.frame_sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.frame_sockfd.bind(frameserver_addr)
    
    def serve_forever(self):
        '''为httpserver提供连接'''
        self.frame_sockfd.listen(5)
        print("Listen the port %d" % frame_port)
        while True:
            try:
                frame_connfd,frame_addr = self.frame_sockfd.accept()
            except KeyboardInterrupt:
                self.frame_sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:",e)
                continue
            # 创建线程处理客户端请求
            clientThread = Thread(target = self.frame_handle,args = (frame_connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
        
    def frame_handle(self,frame_connfd):
        '''具体处理客户端请求'''
        # 接收客户端请求
        while True:
            method = frame_connfd.recv(4096).decode()  
            getRequest = frame_connfd.recv(4096).decode()
            if method == 'GET':
                if getRequest == '/' or getRequest[-5:] == '.html':
                    response = self.get_html(getRequest)
                else:
                    response = self.get_data(getRequest)
            elif method == 'POST':
                pass
            frame_connfd.send(response.encode())
            frame_connfd.close()

    def get_html(self,getRequest):
        '''解析网页请求'''
        if  getRequest == '/':
            filename = self.pape + '/index.html'
        else:
            filename = self.pape + getRequest
        print("filename:",filename)
        try:
            f = open(filename)
        except Exception:
            # 没找到网页
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += '\r\n'
            responseBody = 'Sorry,not found the page'
        else:
            # 如果找到网页则返回网页
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            # 无论成功或者失败都返回内容
            response = responseHeaders + responseBody
            return response

    def get_data(self,getRequest):
        '''如果要获取的不是html网页，可提供有限数据'''
        # for url,func in urls:
            # if getRquest == url:
            #   func()
        # return '404'
        # 可提供的数据关键字仅限在urls中
        urls = ['/time','/tedu','/python']
        if getRequest in urls:
            # 标准格式中请求必须包含了下列三项
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            # 请求体
            if getRequest == "/time":
                responseBody = time.ctime()
            elif getRequest == "/tedu":
                responseBody = 'Tedu python'
            elif getRequest == '/python':
                responseBody = 'python 开发'
        else:
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += "\r\n"
            responseBody = 'No Data'
        response = responseHeaders + responseBody
        return response

if __name__ == '__main__':
    frameserver = Web_Frame(frameserver_addr,static_dir)
    frameserver.serve_forever()   # 启动框架应用程序    