#此示例示意关键字传参
def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)
myfun1(c=300,b=200,a=100 ) #可无序传参
myfun1(c=300,b=200,b=100 ) #不可重复传参
myfun1(c=300,b=200,) #不可重复缺少参数
myfun1(c=300,b=200,d=200) #不可在没有对应参数的情况下传参