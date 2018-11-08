# 看下列程序输出有哪些不同
L = [2,3,5,7]
L2 =[x * 10 for x in L]     #已经是静态数据了,生成了新的列表[]
it = iter(L2)
print(next(it))   # 20
L[1] = 30
print(next(it))   # 30


# 第二段程序
L = [2,3,5,7]
L2 =(x * 10 for x in L)    # 二道贩子,只是有个生成器表达式
it = iter(L2)              # 现用现生成
print(next(it))            # 20
L[1] = 30
print(next(it))            # 300