# #1写一个表达式:
# fx=lambda n:
# 此表达式创建的函数判断n这个数的2次方+1能否被5整除,
# 如果能返回True,不能返回False
# 如:
#     print(f(3))   #True
#     print(f(4))   #False
fx=lambda n:(n**2+1) % 5 == 0
fx=lambda n:True if (n**2+1) % ==0 else False
