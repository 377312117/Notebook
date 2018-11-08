#此示例示意sorted的用法
L = [5,-2,-4,0,3,1]
L2 = sorted(L)   #[-4,-2,0,1,3,5]
print("L2=",L2)
L3=sorted(L,reverse=True)
print("L3=",L3)  #[5,3,1,0,-2,-4]
#依照绝对值排序
L4=sorted(L,key=abs)  #[0,1,-2,3,-4.5]
#依照长度排序
L=["Tom","Tyke"....]
L5=sorted(L,key=len)
L6=sorted(name)