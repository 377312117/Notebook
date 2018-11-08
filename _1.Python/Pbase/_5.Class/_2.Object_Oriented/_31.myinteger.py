# 此函数示意数值转换重写
class MyInteger:
    def __init__(self,value):
        self.data = int(data)
    def __int__(self):
        """此方法必须返回整数"""
        return self.data
a1 = MyInteger("100")
i = int(a1)
print(i)
