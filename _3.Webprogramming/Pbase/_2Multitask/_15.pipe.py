from multiprocessing import Pipe,Process
import os,time


#创建管道对象
fd1,fd2 = Pipe()

# 创建向管道发送内容的函数
def fun(name):
    time.sleep(3)
    # 向管道写入内容
    fd1.send(name)

jobs = []

# 创建进程并且调用发送函数
for i in range(5):
    p = Process(target = fun,args = (i,))
    jobs.append(p)
    p.start()    #进程开始运行

#接收
for i in range(5):
    data = fd2.recv()
    print(data)

#回收
for i in jobs:
    i.join()