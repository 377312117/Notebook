from multiprocessing import Queue 
from time import sleep

# 创建消息队列
q = Queue(3)


q.put(1)           # 往里放内容还没那么快
sleep(0.1)
print(q.empty())   # 该句执行很快,,如果不设置延时,会报True
q.put(2)
q.put(3)
print(q.full()) 
# q.put(4,True,timeout=3)    #超时3秒检测是否阻塞
print(q.get())  # 先进先出 1