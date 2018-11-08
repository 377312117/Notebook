#此示例示意生成器函数的定义和使用
def myyield():
    """这是一个生成器函数,
        此函数用来动态生成2,3,5,7"""
    yield 2     #一旦出现yield,则此函数成为一个生成器函数
    yield 3
    yield 5
    yield 7
# 用来迭代器访问这个生成器函数
gen = myyield()   # 生成器函数调用将返回一个生成器
print(gen)    # gen 是一个生成器对象
it = iter(gen)   #拿到迭代器
print(next(it))   # 2
print(next(it))   # 3
print(next(it))   # 5
print(next(it))   # 7
# print(next(it))   # StopIteration

print("以下用for语句访问生成器")

for x in myyield():
    print(x)