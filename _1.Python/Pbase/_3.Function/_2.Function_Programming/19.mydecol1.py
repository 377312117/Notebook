# 此示例示意函数装饰器的使用
def mydeco(fn):
    def fx():
        print("--------这是fn被调用之前--------")
        fn()
        print("--------这是fn被调用之后--------")
    return fx
@mydeco
def myfunc():
    print("myfunc被调用!")
#以上@mydeco等同于在def myfunc之后加了如下语句
# myfunc = mydeco(myfunc)
myfunc()