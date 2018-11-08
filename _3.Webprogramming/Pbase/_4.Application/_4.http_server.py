# coding = utf-8
# 此服务器示意了一个简单的网页服务器
'''HTTP Server 2.0
多线程并发
可以做request解析
能够返回简单的数据
使用类进行封装
'''

from socket import *
from threading import Thread
import sys
import time

class HTTPServer(object):
    '''封装具体的http server功能'''
    def __init__(self, server_addr, static_dir):
        '''添加用户属性'''
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        # 创建套接字
        self.create_socket()

    def create_socket(self):
        '''为不同的服务端创建连接套接字'''
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)


    def serve_forever(self):
        '''为不同客户端提供连接'''
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:",e)
                continue
            # 创建线程处理客户端请求
            clientThread = Thread(target = self.handle,args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
            
    def handle(self,connfd):
        '''具体处理客户端请求'''
        # 接收客户端请求
        request = connfd.recv(4096)
        # 按行切割,得到一个由响应整体分割而成的的列表，
        # 其中第0个元素是类别，内容，协议版本
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),":",requestHeaders[0])
        # 获取具体内容，getRequest是请求内容，以空格分隔开
        getRequest = str(requestHeaders[0]).split(" ")[1]
        # split() : 将字符串以括号内的字符作为分隔符，得到一个列表
        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()

    def get_html(self,connfd,getRequest):
        '''给客户端发送网页'''
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest
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
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        '''如果要获取的不是html网页，可提供有限数据'''
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
        connfd.send(response.encode())        


# 本模块作为主函数时则执行下列语句
if __name__ == "__main__":
    # 用户自己设定服务器IP
    server_addr = ("0.0.0.0",8000)
    # 需要为用户提供网页位置
    static_dir = './static'
    # 创建服务器
    httpd = HTTPServer(server_addr,static_dir)
    # 启动服务器
    httpd.serve_forever()
