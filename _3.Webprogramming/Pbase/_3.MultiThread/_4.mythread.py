from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    # 需要什么就把什么搬过来,与需要完成的类的参数相对应
    def __init__(self,target,args=(),kwargs ={},name = "Thread-1"):
        # 将参数变为属性
        self.target = target
        self.args = args
        self.kwargs = kwargs
        # 继承父类__init__方法
        super().__init__()
    def run(self):
        # *号传参的各项逐一传递,**传参是将参数按照键值一一传递
        self.target(*self.args,**self.kwargs)

# 测试函数
def player(sec,song):
    for i in range(2):
        print("Playing %s:%s" % (song,ctime()))  
        sleep(sec)  

t = MyThread(target = player,args =(3,),kwargs = {"song":"凉凉"},name = "tedu")
t.start()
t.join()

