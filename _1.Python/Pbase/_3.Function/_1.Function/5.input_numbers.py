# 写一个函数 input_numbers,如下:
# def input_numbers()
# ....
# 此函数用于获取用户循环输入的正整数,当用户输入负数的时候结束输入
# 将用户输入的数字用列表的形式返回,再用内建函数max,min,sum求出
# 用户输入数的最大值,最小值以及和


def input_numbers():
    L=[]
    while True:
        s=int(input("请输入正整数:"))
        if s<=0:
            break    #或者直接return
        else:
            L.append(s)
    return L   
l=input_numbers()
print(l)
print("用户输入的最大数是:",max(l))
print("用户输入的最小数是:",min(l))
print("用户输入的数的和是:",sum(l))