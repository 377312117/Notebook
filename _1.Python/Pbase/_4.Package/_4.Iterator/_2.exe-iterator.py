# 有一个集合:
s = {"唐僧","悟空","八戒","沙僧"}
    # 用for语句遍历所有元素:
    # for x in s:
    #     print(x)
    # else:
    #     print("遍历结束")
    # 请将上面的for语句改写为while语句和迭代器实现
it = iter(s) 
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("遍历结束")
        break