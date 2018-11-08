#观察下面函数执行结果是什么?
def goodbye(L):
    for x in L:
        print("再见:",x)
def hello(L):
    for x in L:
        print("您好:",x)
def fx(fn,L):
    fn(L)
fx(goodbye,["Tom","Jerry","Spike"])
# 再见:Tom
# 再见:Jerry
# 再见:Spike


           