# 写一个函数,mysum可以传入任意个数字的实参,此函数调用将返回实参的和
def mysum(*args):
    s=0
    for i in args:
        s+=i
    return s      
print(mysum())      #0
print(mysum(1,2,3))  #6