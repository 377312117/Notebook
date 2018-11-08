# 已知有列表
L = [2,3,5,7,10,15]
# 1.写一个函数,让此函数能动态提供数据,数据为源列表的的平方+1
# 2.写一个生成器表达式,让此函数能动态提供数据,数据为源列表的的平方+1
# 3.生成1个列表,此列表的数据为源列表的数字的平方+1

# 问题1
# def myeven(lst):
#     for x in lst:
#         yield x**2+1
# evens = list(myeven(L))    #list从中取出数据组成列表
# print(evens)

# 问题2
L1 = list((x ** 2+1 for x in L))
# (x ** 2+1 for x in L) 是生成器表达式,list拿数据
print((x ** 2+1 for x in L))
# <generator object <genexpr> at 0x7f0f164a68e0>
print(L1))