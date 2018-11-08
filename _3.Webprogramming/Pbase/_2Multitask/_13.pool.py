# 此示例示意pool 创建进程池的用法
from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime() 
# 创建进程池
pool = Pool(processes = 3)  # 默认数为几个cpu为几个进程

result = []
# 向进程池添加事件
for  i in range(10):
    msg = "hello %d" % i
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r)
# 关闭进程池
pool.close()

#回收进程池
pool.join()
for i in result:
    print(i.get())   # 可以获取进程事件函数的返回值
  