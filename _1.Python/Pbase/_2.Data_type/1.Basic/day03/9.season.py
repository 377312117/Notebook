#输入季度显示月份
while True:
    season=int(input("请输入１～４季度："))
    if season==1:
        print("%d季度有1,2,3月"%season)
    elif season==2:
        print("%d季度有4,5,6月"%season)
    elif season==3:
        print("%d季度有7,8,9月"%season)
    elif season==4:
        print("%d季度有10,11,12月"%season)
    else:
        print("输入错误,请重新输入：")