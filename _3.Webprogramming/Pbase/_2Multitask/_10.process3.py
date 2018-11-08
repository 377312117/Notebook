import multiprocessing as mp
from time import sleep

# 编写进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working...")

p = mp.Process(target = worker,args = (2,"Levi"))
# 也可以传关键字参数,args = (2,),kwargs ={"name":"Levi"}   #但是顺序传参需要是一个元组

p.start()
p.join(4)
print("====================")