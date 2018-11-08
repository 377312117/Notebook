# 用于制作添加元素的函数
def input_studentinfo():
    l=[]
    L1=["name","age","score"]
    while True:
        dic={}
        s1=input("please input name:")
        if s1 == "":
            break
        s2=int(input("please input age:"))
        s3=int(input("please input score:"))
        L2=[s1,s2,s3]
        for x in range(0,3):
            dic[L1[x]]=L2[x]
        l.append(dic)
    return l

class student:
    infos = []
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s