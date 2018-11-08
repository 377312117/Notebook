# 此示例示意super函数的用法
class A:
    def work(self):
        print("A.work被调用")
class B(A):
    def work(self):
        """此方法覆盖了父类的work方法"""
        print("B.work被调用")
    def mywork(self):
        # 调用自己(B类)的方法
        self.work()
        # 调用父类(A类)的方法
        super(B,self).work()
        # 等同于 super().work()  一定要在方法里用

b=B()
b.work()

#调用父类被覆盖的方法
A.work(b)   # A.work被调用 ,一定要知道父类是谁
super(B,b).work() # A.work被调用