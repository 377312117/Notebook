#定义空列表，以便于往里面加值
L=[]
#循环输入值以求累加
while True:
    #定义a变量往里添值，不需要变为列表
    a=input("请输入列表元素：")
    #规定选择条件，一旦输入为空终止循环
    if a=='':
        break
    #在循环结构而未进入选择结构时不断累加，
    #为列表增加新元素
    L+=[a]
#break后直接跳出循环，执行下一条语句
print(L)
      
