# L=[1,3,2,1,6,4,2,.....98,82]
# 将列表L中出现的数字存入到另一个列表Ｌ２中，要求
# 1)重复出现多次只在L2中保留一份，
# 2)将列表中出现两次的数字存于Ｌ３中，在L3中只保留一次，

# L=[]
# L1=[]
# L2=[]
# while True:
#     s=int(input("请添加元素:"))
#     if L.count(s)==0:
#         L1.append(s)
#     if s<=0:
#         break
#     else:
#         L.append(s)
# print(L)
# print(L1)   
# for x in L:
#     if L.count(x)==2 and x not in L2:
#         L2.append(x)
# print(L2)

# 1)重复出现多次只在L2中保留一份，
L=[1,2,3,1,6,4,2,6,6,98,82]
#准备存放出现过的数字
L2=[]
#将所有数遍历一遍
for x in L:
    #如果是第一次出现,则添加到L2列表中
    if x not in L:
        L2.append(x)
print(L2)

# 2)将列表中出现两次的数字存于Ｌ３中，在L3中只保留一次，
L3=[]
for x in L:
    #出现次数为2,且x不在L3中
    if L.count(x)==2 and x not in L3:
        L3.append(x)
print(L3)