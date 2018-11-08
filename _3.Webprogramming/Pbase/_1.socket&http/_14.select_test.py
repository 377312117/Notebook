from select import select
from socket import *


s = socket()
s.bind(("0.0.0.0",8888))
s.listen(3)

# 关注套接字IO
print("监控IO")
rs,ws,xs = select([s],[],[],3)
print("处理IO")
