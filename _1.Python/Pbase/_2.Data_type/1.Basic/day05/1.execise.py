# "%-010d" % 123
s1=input('请输入第一行：')
s2=input('请输入第二行：')
s3=input('请输入第三行：')
max_len=input("请输入长度：")
print("%+"(max_len)"+"s" % s1)
print("%(max_len)s" % s2)
print("%(max_len)s" % s3)