from socket import *
import struct

s = socket()
s.bind(("0.0.0.0",8899))
s.listen(5)

# 确定数据结构
st = struct.Struct("i5sf")
c,addr = s.accept()
data = c.recv(1024)

# 解析数据
data = st.unpack(data)    调出st实例的方法
print(data)

c.close()
s.close()

