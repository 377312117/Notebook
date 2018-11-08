from multiprocessing import Queue,Process
from time import sleep

# 创建消息队列
q = Queue()


def fun1():
    for i in range(10):
        sleep(1)
        q.put((1,2))

def fun2():
    for i in range(10):
        sleep(1.5)
        a,b = q.get()
        print("sun =",a+b)
p1 = Process(target = fun1)
p2 = Process(target = fun2)

p1.start()
p2.start()
p1.join()
p2.join()