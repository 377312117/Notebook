# 已知有列表:
L=[[3,5,8],10,[[13.14],15,18],20]
# 1)写一个函数print_list(lst)  打印出所有的数字,即:
# print_list(L)   #打印3,5,8,10....
# 2)写一个函数sum_list(lst)  返回这个列表中素有数字的和
#  print(sum_list(L))  #106
# 注:
#     type(x)  可以返回一个变量的类型:,进行判断
# 递归解决
def get_num(lst):
    for x in lst:
        if type(x) is int:
            print(x)
        elif type(x) is list:
            get_num(x)
get_num(L)
def sum_list(lst):
    s=0
    for x in lst:
        if type(x) is int :
            s+=x
        else:
            s+=sum_list(x)
    return s
print(sum_list(L))