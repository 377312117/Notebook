#  2. 子集写一个mylist类,实现重写len,和str,让Mylist类型变为可迭代对象

# 自建一个mylist,实现list大部分功能,重写len,str,以及让Mylist编程一个可迭代对象
class mylist:
    #对自建的列表进行初始化操作
    def __init__(self,iterable=()):
        self.data = [x for x in iterable]
    def __str__(self):
        return ("数字%d") % self.data
    def __len__(self):
    