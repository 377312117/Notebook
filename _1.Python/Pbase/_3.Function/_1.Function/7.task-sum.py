# 2.定义两个函数:
#  sum3(a,b,c)  用于返回3个数的和
#  pow3(x)  用于返回x的3次方
# 1)计算1的立方+2的立方+3的立方的和
# 2)计算1+2+3的和的立方
def sum3(a,b,c):
    s=a+b+c
    return s
def pow3(x):
    p=x**3
    return p
print("1的立方+2的立方+3的立方",pow3(1)+pow3(2)+pow3(3))
print("1+2+3的和的立方:",pow3(sum3(1,2,3)))