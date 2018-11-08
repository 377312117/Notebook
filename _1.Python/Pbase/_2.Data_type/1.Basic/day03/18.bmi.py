# BMI=体重／身高的平方
# BMI<18.5  体重过轻
# 　１８．５～２４　正常
# 　大于２４．　过重
#  输入一个体重，并输出体重状况
weight=float(input("请输入您的体重(kg)："))
height=float(input("请输入您的身高(m)："))
BMI=weight/height**2
if 0<=weight<=18.5:
    print("BMI值为%f,您的体重过轻"%BMI)
elif 18.5<weight<=24:
    print("BMI值为%f,您的体重正常"%BMI)
elif weight>24:
    print("BMI值为%f,您的体重过重"%BMI)
else:
    print("您输入数值有误")