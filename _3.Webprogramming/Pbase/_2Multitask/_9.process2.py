import multiprocessing as mp
from time import sleep
import os

# 编写进程函数
def th1():
    sleep(1)
    print("吃饭")
    print(os.getpid(),"--",os.getppid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getpid(),"--",os.getppid())

def th3():
    sleep(3)
    print("打豆豆")
    print(os.getpid(),"--",os.getppid())


things = [th1,th2,th3]
process = []

for th in things:
    p = mp.Process(target = th)
    process.append(p)   #保留每次创建的进程对象
    p.start()

# 在start 和join之间可以利用父进程做一些事情
# 不过一般会牺牲父进程不做具体事情,让子进程进行工作

for i in process:
    i.join()   #如果不回收会产生僵尸进程