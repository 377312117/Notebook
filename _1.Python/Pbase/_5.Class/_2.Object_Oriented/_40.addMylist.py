# 实现两个自定义列表的列表相加操作
class Mylist:
    def __init__(self,iterable=()):
        self.data = list(iterable)
    def __repr__(self):
        return "Mylist(%s)" % self.data
    def __add__(self,other):
        return Mylist(self.data + other.data)
    def __mul__(self,other):
        return Mylist(self.data * other)
L1 =Mylist(range(1,4))
L2 =Mylist(range(4,7))
