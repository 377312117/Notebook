# 此函数示意函数重写
class Mylist:
    """创建一个自定义列表,此Mylist内部用列表来存储数据"""
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "Mylist(%s)" % self.data
    def __len__(self):
        """此方法必须返回整数"""
        return self.data.__len__()
    def __abs__(self):
        """此方法把self的所有元素取绝对值,返回全为正数的自定义列表"""
        lst = (abs(x) for x in self.data)
        L = Mylist(lst)
        return L
myl =Mylist([1,-2,3,-4])
print(myl)
myl2 = Mylist()
print(myl2)