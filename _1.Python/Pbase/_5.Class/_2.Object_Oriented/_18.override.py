# 此示例示意覆盖的语法
class A:
    def work(self):
        print("A.work被调用")
class B(A):
    def work(self):
        """此方法覆盖了父类的work方法"""
        print("B.work被调用")

b=B()
b.work()

#调用父类被覆盖的方法
A.work(b)   # A.work被调用 ,一定要知道父类是谁