def f1():
    print("hello f1")
def f2():
    print("hello f2")
f1,f2=f2,f1
f1()  #语句块交换,输出f2