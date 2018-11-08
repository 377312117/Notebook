# 输入一段字符串,打印这个字符串中出现的字符以及出现的过的次数
# 思路:字符是键,次数是值
# 方法1:
s=input("请输入字符串:")
# d={}
# for x in s:
#     #如果存在,进行+1操作
#     if x in d:    
#         d[x]+=1
#     #如果不存在进行键值对的创建
#     else:
#         d[x]=1
# print(d)
# for k,v in d.items():
#     print(k,":",v,"次")
# 方法2:
L=[]
for ch in s:
    #如果ch没有在L中,说明第一次出现,放在L中
    if ch not in L:
        L.append(ch)
#print(L)
for ch in L:
    print(ch,":",s.count(ch),"次")
