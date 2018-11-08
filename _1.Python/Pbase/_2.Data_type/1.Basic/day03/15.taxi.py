# 计算北京出租车计价器
# 收费标准：
# 　　３公里１３元
#     基本单价２．３元
#     空驶费：１５公里后３．４５元／公里
#  要求：
#     输入公里数，打印出费用金额（以元为单位四舍五入）
miles=float(input("请输入公里数："))
intprice=13
if 0<miles<=3:
    pay=intprice
    pay=round(pay)
    print("您的费用为%d元"%pay)
elif 3<miles<=15:
    pay=2.3*(miles-3)+13
    pay=round(pay)
    print("您的费用为%d元"%pay)
elif miles>15:
    pay=2.3*(15-3)+13+(miles-15)**3.45
    pay=round(pay)
    print("您的费用为%d元"%pay)
else:
    print("您的输入有误")

