#写一个函数mymax3,返回三个数中最大的一个值
# def mymax3(a,b,c)
    # ... 
# print(mymax3(100,300,200))    #123
# print(mymax3(ABC","123","abc")) #abc
def mymax3(a,b,c):
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    return m
print(mymax3(100,300,200)) 
print(mymax3(ABC","123","abc"))