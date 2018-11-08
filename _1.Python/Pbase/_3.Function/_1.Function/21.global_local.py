#此示例示意global() 和 locals()函数
a,b,c=1,2,3
def fn(c,d):
    e=300
    #有三个局部变量
    print("locals()返回:",locals())
    print("globals()返回:",globals())
    print("globals()返回:",globals())
    print(c)    #访问局部变量100
    print(globals()["c"])
fn(100,200)