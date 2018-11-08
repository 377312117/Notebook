# 此示例示意zip函数的实现
def myzip(iter1,iter2):
    # 先拿到两个对象的迭代器
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        try:
            a = next(it1)
            b = next(it2)
            yield(a,b)
        except StopIteration:
            return