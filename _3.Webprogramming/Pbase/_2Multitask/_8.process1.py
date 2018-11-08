import multiprocessing as mp
from time import sleep
import os
a = 1

# 编写进程函数
def fun():
    # global a
    # a = 100000
    print("子进程事件")
    print("子进程a=",a)

# 创建进程对象
p = mp.Process(target = fun)

# 启动进程
p.start()
sleep(2)
print("父进程时间")
# 回收进程
p.join()
print("父进程 a = ",a)   # 父进程不受子进程影响,即使是子进程定义了全局变量