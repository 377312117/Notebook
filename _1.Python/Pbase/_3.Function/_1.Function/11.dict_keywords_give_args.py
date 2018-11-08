#此示例示意字典关键字传参
def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)
d1={"c":33,"b":22,"a":11}
#两个星号目的是拆解字典,等同于:myfun1(a=11,b=22,c=33)
myfun1(**d1)
d1={"c":33,"b":22,"a":11} #可无序传参
d1={"c":33,"b":22,"d":11} #错误,不可在没有对应参数的情况下传参
d1={"c":33,"b":22,} #错误,不可重复缺少参数
d1={"c":33,"b":22,"a":11,"d"=44} #错误,不可增加参数