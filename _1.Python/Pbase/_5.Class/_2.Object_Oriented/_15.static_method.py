# 此函数示意static_method的用法
class A:
    @staticmethod
    def myadd(a,b):
        """这是静态方法,既不需要用类也不需要实例"""
        return a + b
# 用类来调用静态方法
print(A.myadd(100,200))   # 300  A未传参
a =A()
# 用此类的实例来调用静态方法
print(a.myadd(300,400))   # 700  