#写一个函数min_max(...)函数
# 此函数至少传一个参数,并返回全部的这些数的最大值最小值
# 形成元组,最小值在前,最大值在后,调用此函数得到最大最小函数并打印出来
# def min_max(*args):
#     if args==():
#         print("您输入有误!")
#         return()
#     else:
#         a=min(args)
#         b=max(args)
#         return a,b
# print(min_max(10,20,30))
# x,y= min_max(8,6,4,3,9,2,1)
# print("最小值是:",x)
# print("最大值是:",y)
# print(min_max())   #没有实参报错
def min_max(a,*args):
    # print("a=",a)    10
    # print("args",a)  20,30
    zuixiao=a
    for x in args:
        if x<zuixiao:
            zuixiao = x
    zuida=a
    for x in args:
        if x>zuida:
            zuida = x 
    return (zuixiao,zuida)