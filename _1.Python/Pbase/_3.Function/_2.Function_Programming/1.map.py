def power2(x):
    print("power2被调用,x=",x)
    return x**2
 #生成可迭代对象,此可迭代对象可以生成1~9的自然数的平方
 
for x in map(power2,range(1,10)):
#先从range中拿数据,带入函数power2中,返回函数得到的值,此map函数重复调用括号内的函数
    print(x)  #1,4,9,16