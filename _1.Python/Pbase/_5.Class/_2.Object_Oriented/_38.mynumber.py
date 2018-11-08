# 此函数示意 运算符重载
class Mynumber:
    """自定义数字"""
    def __init__(self,value):
        self.data = value 
    def __repr__(self):
        return ("Mynumber (%d)" )% self.data 
    def __add__(self,other):
        print("__add__被调用")
        v = self.data + other.data
        obj = Mynumber(v)
        return obj
n1 = Mynumber(100)
n2 = Mynumber(200)
n3 = n1.__add__(n2) 
n3 = n1 + n2  
print(n1)
n1 = n1.__add__(n2)   # Mynumber(300)
print(n1,"+",n2,"=",n3)