#已知五位朋友,
#第五位朋友说他比第四位朋友大两岁
#第四位朋友说他比第三位朋友大两岁
#第三位朋友说他比第二位朋友大两岁
#第二位朋友说他比第一位朋友大两岁
#第一位朋友说他10岁
def getage(n): #求第n个人的年龄
    if n == 1:
        return 10
    return 2 + getage(n-1)
print(getage(12))  #18