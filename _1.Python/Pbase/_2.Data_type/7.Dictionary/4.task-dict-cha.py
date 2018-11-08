# #已知两个等长列表,写程序变为相应字典
# list1=[1001,1002,1003,1004]
# list2=["Tom","Jerry","Spike","Tyke"]
# 写程序生成如下字典:
# {"Tom":1001,"Jerry":1002,"Spike":1003,"Tyke":1004}
list1=[1001,1002,1003,1004]
list2=["Tom","Jerry","Spike","Tyke"]
dic={}
# 方法1:
# for x in range(0,4):
#     dic[list2[x]]=list1[x]
# print(dic)
# 方法2:字典推导式
d={list2[i]:list1[i] for i in range(0,4)}