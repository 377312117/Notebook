# #定义很多个函数,每个函数求x**y,y是可变的
# # 示例:
# def pow2(x):
#     return x**2
# def pow3(x):
#     return x**3
# ...
# def pow99(x):
#     return x**99
#经下用闭包来实现
def make_power(y):
    def fn(x):
        return x**y
    return fn
pow2=make_power(2)     #pow2绑定了一个闭包
print("5的平方是:",pow2(5))
