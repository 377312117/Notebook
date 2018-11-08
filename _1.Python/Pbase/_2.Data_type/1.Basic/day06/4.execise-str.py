#输入一段字符串，判断您的字符串中有几个中文字符
a=input("请输入字符串：")
count=0
for x in a:
    ch=ord(x)
    if ch>127:
        print(x)
        count+=1
print(count)