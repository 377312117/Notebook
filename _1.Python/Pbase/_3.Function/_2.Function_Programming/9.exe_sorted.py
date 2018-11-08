#names=["Tom","Jerry","Spike","Tyke"]
#排序的依据是"moT","yrreJ","ekipS","ekyT"
# #结果是:
names=["Spike","Tyke","Tom","Jerry"]
# (注:如果没有现成的函数可用,需要自己写函数)
#传入的是列表（可迭代对象）中的每个字符串
def fk(s):
    r=s[::-1]
    return r
L1=sorted(names,key=fk)
print(L1)