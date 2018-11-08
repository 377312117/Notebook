#看懂下面程序在做什么
def fx(f,x,y):
    print(f(x,y))
fx((lambda a,b:a+b),100,200)
#使用fx函数,将lambda a,b:a+b带入f,100带入x,200带入y
fx((lambda a,b:a**b),3,4)
#使用fx函数,将lambda a,b:a**b带入f,100带入x,200带入y