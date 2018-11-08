# 此示例示意函数重写
class MyNumber:
    """此函数定义一个自定义的数值类型"""
    def __init__(self,value):
        self.data = value   #Data数据
    def __str__(self):
        """重写object类中的__str__.(obj)"""
        return "数字%d" % self.data
    def __repr__(self):
        """重写object类中的__str__.(obj)"""
        return "数字%d" % self.data
n1 = MyNumber(100)
s1 = str(n1)    # s1 = n1.__str__()
s2 = repr(n1)
print(s1)
print(s2)