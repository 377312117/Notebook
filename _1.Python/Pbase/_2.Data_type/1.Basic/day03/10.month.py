#输入月份显示季度
while True:
    month=int(input("请输入１～12月份："))
    if 1<=month<=3:
        print("%d月属于１季度"%month)
        break
    elif 4<=month<=6:
        print("%d月属于2季度"%month)
        break
    elif 7<=month<=9:
        print("%d月属于3季度"%month)
        break
    elif 10<=month<=12:
        print("%d月属于4季度"%month)
        break
    else:
        print("输入错误，请重新输入：")
