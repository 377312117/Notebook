v=100
def f1():
    # global v   #全局声明
    v=200
    # global v   #不能先赋值,后声明,此做法不符合规则    
    v=300
f1()  #虽然执行了函数,但是只在局部作用域内创建了v=200,
print("v=",v)
#返回 全局变量:v=100

v=100
def f1(v):
    global v  #会报错,global变量列表里的变量名不能出现在函数的形参列表里
    print(v)
f1()  
print("v=",v)
