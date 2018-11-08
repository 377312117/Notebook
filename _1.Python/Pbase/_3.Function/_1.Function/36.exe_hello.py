# 写一个函数hello,部分代码如下:
count=0
def hello(name):
    print("您好",name)
    global count   #全局声明,引用全局变量
    count+=1
# 当调用hello函数时,全局变量count自动做加1操作
# 来记录hello被调用的次数
# 如:
hello("Tom")
hello("Jerry")
hello("hello函数共被调用%d次"% count)
