'''
httpserver相关配置
凡是用户自己决定的东西都放在配置文件里
'''

# please settings here

HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

# 配合框架的IP地址
frame_ip = '127.0.0.1'
frame_port = 8080
frame_address = (frame_ip,frame_port)
frameserver_addr = (HOST,frame_port)