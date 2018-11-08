# 用列表推导式生成如下列表
# [[1,2,3],[4,5,6],[7,8,9]]
# L1=[x for x in range(1,4)]
# L2=[x for x in range(4,7)]
# L3=[x for x in range(7,10)]
# L=[L1,L2,L3]
# print(L)
# 方法１：
# L=[[x,x+1,x+2] for x in range(1,8,3)]
# print(L)
# 方法２：
l1=[[y for y in range(x,x+3)] for x in range(1,8,3)]
print(l1)
