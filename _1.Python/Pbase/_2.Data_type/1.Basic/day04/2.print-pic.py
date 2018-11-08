# 写一个程序，打印一个高度为４行的矩形，
# 宽度需使用输入函数输入
width=int(input("请输入矩形宽度:"))
height=int(input("请输入矩形高度:"))
i=2
print("#"*width)
while i<height:
    print("#"+" "*(width-2)+"#")
    i+=1
print("#"*width)