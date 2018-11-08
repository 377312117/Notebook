def say_hello():
    print("hello world")
    print("hello Tarena")
    return[1+2+3]   #等同于return None
    print("hello everyone")
# say_hello()  #调用一次say_hello
r=say_hello()  
print(r)      #返回[6]
#用r绑定该引用关系,绑定了return,r将返回return后面的表达式
print("程序结束")