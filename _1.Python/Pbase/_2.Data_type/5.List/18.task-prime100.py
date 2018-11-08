# 计算１００以内所有的素数，
# 将素数存于列表中，打印列表中的素数
#创建容器,往里面添加数据并得到目标列表
L=[]
#遍历100以内的数,然后判断100以内所有素数并加入列表中
for x in range(1,101):
    #遍历2到x之间的数,查询x是否是素数
    for y in range(2,x):
        if x % y==0:
            #一旦出现能整除的数直接略过
            break
    #遍历完都没有可除的数,代表着该数是素数
    else:
        L.append(x)
print(L)

# 方法2
L=[]
for x in range(1,101):
    isprime=True
    if x<2:
        isprime=False
    else:
        for i in range(2,x):
            if x%i ==0:
                isprime=False
                break
    if isprime:
        L.append(i)
print(L)
            
