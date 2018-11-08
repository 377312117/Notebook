# 一个球从100米高空落下,每次落地后反弹高度为原高度的一半再落下
    # 写程序算出皮球在10次落下时反弹多高
    # 打印10次后球共经历多少米的路程
print(100* 1/2**10)
# 方法2:
def get_last_height(meter,times):
    """根据小球的初始高度和次数,返回最后的反弹高度"""
    for x in range(times):
        meter /= 2
    return meter
print("球第十次落地后高度是:",get_last_height(100,10))

#方法2
def get_distance(meter,times):
    """根据循环求总行程"""
    s = 0  #记录总行程
    for x in range(times):
        s += meter
        meter /= 2
        s += meter
    return s
print(get_distance(100,10))
print(100+100*sum(map(lambda x:1/2**(x-1),range(1,11))))