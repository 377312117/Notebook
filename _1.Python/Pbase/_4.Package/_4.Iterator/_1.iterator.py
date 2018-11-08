# 此示例示意iterator的用法
L = [1,3,5,7]
it = iter(L)  #让iter 函数从L中获取迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
# 等同于:
# for x in L:
#     print(x)