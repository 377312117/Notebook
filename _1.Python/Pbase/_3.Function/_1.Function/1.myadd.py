#写一个函数myadd,此函数中的传参列表中有两个参数x,y,此函数
# 的功能是打印x+y的和
# 如:
#     def myadd(...):
#         ...    
#     myadd(100,200)    #打印300
#     myadd("ABC","123") 打印 ABC123
def myadd(a,b):
    s=a+b
    print("两者之和为:",s)
myadd(100,200)
myadd("ABC","123")