from socketserver import *
import time

class Server(ForkingMixIn,TCPServer):
    pass

# 处理具体请求
class Handler(StreamRequestHandler):
    # 具体处理方法
    def handle(self):
            print("Connect from",self.client_address)
            while True:
                data = self.request.recv(1024)
                if not data:
                    break
                print(data.decode())
                self.request.send("Receive:".encode())
                
if __name__ == "__main__":
    server_addr = ("0.0.0.0",8888)
    # 创建服务器对象
    server = Server(server_addr,Handler)
    server.serve_forever() # 启动服务器
    