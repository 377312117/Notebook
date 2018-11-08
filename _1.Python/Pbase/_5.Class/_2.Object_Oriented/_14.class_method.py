# 此示例示意类方法的定义和调用
class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v
    
    @classmethod
    def set_v(cls,value):   # 传进cls中的为类
        cls.v = value   # 设置类变量为 v = value
print(A.v)   # 0 直接访问类变量
value = A.get_v()    # 想调用A 类的方法来取值
print("value =",value)   # 0 

A.set_v(999)
print(A.set_v)    # 999

a = A()   # 创建实例对象
print(a.get_v())   # 借助对象来调用类方法
a.set_v(100)       # 借助对象来设置类变量v,传进的是a.__class__
print(a.set_v(100))   # 
print(a.get_v())   # 100
print(a.v)     # 100