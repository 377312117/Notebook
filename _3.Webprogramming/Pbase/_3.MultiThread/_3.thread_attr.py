from threading import Thread,currentThread
from time import sleep

def fun():
    sleep(3)
    print("执行%s线程" % currentThread().getName())   # 获取线程对象
    print("线程属性测试")



t = Thread(target = fun,name = "Tarena")

# 设置daemon
t.setDaemon(True)
# t.daemon = True

t.start()
t.setName("tedu")   # 修改线程名
print("Thread name:",t.name)    # 获取线程名
print("Thread get name:",t.getName())
print(t.is_alive())   # 线程状态,分支线程一旦结束则为False
print("********主线程结束******")    # 只有分支线程执行结束,整个进程才会结束
t.join()