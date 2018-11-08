# 此示例示意自定义用with管理的对象
class A:
    """此类的对象可用于with语句中"""
    def __enter__(self):
        print("已经进入到with语句内部")
        return self
    def __exit__(self,e_t,e_v,e_tb):
        """e_t用来绑定异常类型
            e_v用来绑定异常对象
            e_tb用来绑定追踪对象,在都没有异常时,三个形参都绑定None"""
        if e_t is None:
            print("已经正常离开with语句")
        else:
            print("是在出异常时走异常流程离开的with语句")
with A() as a:
    print("这是with语句内部的print")
    int(input("请输入整数:"))