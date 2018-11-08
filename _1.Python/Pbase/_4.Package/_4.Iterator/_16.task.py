# 写一个myfilter生成器函数,功能和filter函数功能完全相同
#如
def myfilter(fn,iter1):
    for item in iter1:
        if fn(item) == True:
            yield item
L = [x for x in myfilter(lambda x : x%2,range(10))] 


# 将之前所有练习,重新写一遍