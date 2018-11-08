#此示例示意函数名绑定函数,函数名是变量名
def fn():
    print("hello world")
f1=fn   #fn绑定是该语句块对象
print(f1)    #<function fn at 0x7f441e81ff28>
fn()       # hello world   调用函数
f1()       # hello world
print()    # None