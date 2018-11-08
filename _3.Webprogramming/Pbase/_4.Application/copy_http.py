# 本模块示意http2.0自我复原过程
# 1.了解需求
    # 1.能够支持网页库浏览
    # 2.能够支持多个客户端浏览，创建多线程
    # 3.除了显示网页，还能显示其他一些指定数据
    # 4.可以做到request解析，从而返回不同网页
    # 5.使用类进行封装
# 2.技术分析
    # 1.类的使用和创建，参数的合理选择
    # 2.多线程的运用
    # 3.简单服务器的搭建
    # 4.对于响应的整体结构有个合理的规划
# 3.确认结构
    # 1.创建主函数，分别有创建套接字，链接套接字
    # 2.发送请求，解析请求，根据请求进行反馈，由于是和
    # 浏览器进行连接，所以客户端无需制作，只需要按照
    # 标准的http响应格式进行沟通解析即可
    # 确认调用的模块
from socket import *
from threading import Thread
import sys
import time

class HTTPServer(object):
    '''五大功能皆包括'''
    def __init__(self,server_addr,static_dir):
        self.server_addr = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)
    
    def serve_forever(self,serve_addr,static_dir):
        self.sockfd.listen(5)
        print("listen to the port: %d" % self.port )
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit("连接失败！")
            except  Exception as e:
                print("Error:",e)
            clientThread = Thread(target =self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    
    def handle(self,connfd):
        '''处理客户端的具体请求'''
        request = connfd.recv(4096)
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),":",requestHeaders[0])
        getRequest = str(requestHeaders[0]).split(" ")[1]
        if getRequest =='/' or getRequest[-5:] == ".html":
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
        connfd.close()
    
    def get_html(self,connfd,getRequest):
        if getRequest == "/":
            filename = self.static_dir + "/index.html"
        else:
            filename = self.static_dir + getRequest
        print("filename:",filename)
        try:
            fd = open(filename)
        except Exception:
            # 没找到网页
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders +='\r\n'
            responseBody = "Sorry,not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = fd.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd,getRequest):
        urls = ["/python","/time","/tedu"]
        if getRequest in urls:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "\r\n"
            if getRequest == "/python":
                responseBody = "python 开发"
            elif getRequest == "/tedu":
                responseBody = 'tedu python'
            elif getRequest == '/time':
                responseBody = time.ctime()
        else:
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += '\r\n'
            responseBody  = 'No data'
        response = responseHeaders + responseBody
        connfd.send(response.encode())

def main():
    # 搭建服务器地址 
    server_addr = ("0.0.0.0",8000)
    # 指定网页库
    static_dir = "./static"
    # 创建服务器
    # 难点1 传什么参数进去，等待后续编程确定
    httpd = HTTPServer(server_addr,static_dir)
    # 建立永久循环
    httpd.serve_forever(server_addr,static_dir)

if __name__ == "__main__":
    main()