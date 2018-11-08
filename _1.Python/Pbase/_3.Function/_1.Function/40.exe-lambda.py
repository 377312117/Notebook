#写一个lambda表达式来创建函数,此函数返回形参变量中的最大值
def mymax(x,y):
    l=max(x,y)
    return l
mymax=lambda x,y: x if x>y else y
print(mymax(100,200))
print(mymax("ABC","123"))