# 此示例示意协程的用法
def fun():
    print("启动生成器")
    yield 1
    print('生成器完成')

# 生成器对象
g = fun()
# 或print(next(g))
print(g.__next__())
print(g.__next__())
# 关闭生成器对象
g.close()
