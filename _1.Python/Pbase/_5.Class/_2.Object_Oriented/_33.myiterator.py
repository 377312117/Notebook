# 此示例示意自定义的类定义为可迭代对象
class Mylist:
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    def __repr(self):
        return "Mylist(%s)" % self.data 
    def __iter__(self):
        """此方法要求必须返回迭代器"""
        return Mylist_Iterator(self.data)
class Mylist_Iterator:
    def __init__(self,data):
        # 绑定可迭对象的数据
        self.data = data
        self.cur_index = 0  # 设置迭代器的起始位置
    def __next__(self):
        """此方法用来实现迭代器协议"""
        if self.cur_index >= len(self.data):
            raise StopIteration
        r = self.data[self.cur_index]
        # 将索引值指向下一个数
        self.cur_index += 1
        return r
L = Mylist("ABCD")
print(L)
for x in L:
    print(x)