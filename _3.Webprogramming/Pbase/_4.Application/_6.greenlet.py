from greenlet import greenlet

def test1():
    print(12)
    gr2.switch() # 一旦遇到暂停，则暂停本函数，执行本句的函数
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

# 将两个函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch() # 执行协程test1
