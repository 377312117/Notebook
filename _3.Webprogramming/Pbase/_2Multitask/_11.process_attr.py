import multiprocessing as mp
from time import sleep,ctime

# 编写进程函数
def tm():
    for i in range(4):
        sleep(2)
        print(ctime())

p = mp.Process(target = tm)
p.daemon = True
p.start()

print("Process name",p.name)
print("Process name",p.pid)
print("Process name",p.is_alive())

p.join()