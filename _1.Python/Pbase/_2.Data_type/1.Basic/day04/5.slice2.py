#输入一个字符串判断这个字符串是否为回文
#回文为中心对称的文字
s=input("请输入一个字符串：")
if s==s[::-1]:
    print("%s是回文"%s)
else:
    print("%s不是回文"%s)