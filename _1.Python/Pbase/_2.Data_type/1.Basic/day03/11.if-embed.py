#演示if语句嵌套
n=int(input("请输入月份(1~12)"))
if 1<=n<=12:
    print("该月份为合法月份")
    if n<=3:
        print("春季")
    elif n<=6:
        print("夏季")
    elif n<=9:
        print("秋季")
    else:
        print("冬季")
else:
    print("该月份为不合法月份")