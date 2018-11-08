# 输入很多整数，输入０结束输入，保存于列表L中，
# 将正数存于Ｌ1，负数存于Ｌ2中
# 打印Ｌ１，L2,L3
L=[]
while True:
    s=int(input("请输入整数："))
    if s==0:
        break
    else:
        L.append(s)
L1=[x for x in L if x>0]
L2=[x for x in L if x<0]
print("列表L为：",L)
print("列表L1为：",L1)
print("列表L2为：",L2)
    