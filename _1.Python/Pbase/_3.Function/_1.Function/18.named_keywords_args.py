#此示例示意命名关键字形参的定义方式和调用方法
# def f1(*,c,d):
#     print("c=",d)
#     print("d=",d)
# f1(3,4)    #报错
# f1(d=4,c=3)   #正确

def f2(a,b,*args,c,d):
    #一旦出现*args,后面的都必须是关键字参
    #*args收集多余的位置参数
    print(a,b)
    print(args)
    print(c,d)
f2(1,2,3,4,d=200,c=100)
#  1 2
# (3, 4)
# 100 200

# f2(11,22,33,**{"c":100."d":22})
#