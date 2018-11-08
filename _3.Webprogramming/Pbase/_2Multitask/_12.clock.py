# 此示例示意自定义进程类
from multiprocessing import Process
import time
class ClockProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()    #加载了父类的__init__,默认参数为(子类名,self)
    def run(self):
        for  i in  range(5):
            print("the time is {}".format(time.ctime()))
            time.sleep(self.value)
p = ClockProcess(2)
p.start()   # 会自动运行run方法
p.join()

