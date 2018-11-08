# 练习:
    # 写一个myrange函数,参数可以传递1~3个,实际含义与range相同
    # 此函数返回符合range(..)函数的列表
    # 如:
    #     L=myrange(4)
    #     print(L)  #[0,1,2,3]
    #     L=myrange(4,6)
    #     print(L)  #[4,5]
    #     L=myrange(1,10,3)
    #     print(L)  #[1,4,7]
    #     注:可以调用range
# def myrange(a=0,b=None,c=1):
#     l=range(a,b,c)
#     return l
# L=myrange(4)
# L=myrange(4,6)
# L=myrange(1,10,3)
def myrange(a,b=None,c=None):
    if b is None:
        start=0
        stop=a
    else:
        start=a
        stop=b
    if c is None:
        step=1
    else:
        step=c
    print("开始值:"a)
    print("开始值:"b)
    print("开始值:"c)
    return list(range(start,stop,step))
L=myrange(4)
L=myrange(4,6)
L=myrange(1,10,3)