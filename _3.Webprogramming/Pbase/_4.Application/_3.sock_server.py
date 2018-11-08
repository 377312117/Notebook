from socketserver import *

# 建立多进程
class Server(ForkingMixIn,UDPServer):
    pass

# 处理具体请求
class Handler(DatagramRequestHandler):
    # 具体处理方法
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'Receive')

if __name__ == "__main__":
    server_addr = ("0.0.0.0",8888)
    # 创建服务器对象
    server = Server(server_addr,Handler)
    server.serve_forever() # 启动服务器
    