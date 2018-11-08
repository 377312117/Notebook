#任意输入一段字符串，计算字符a的个数，并打印出来
# 计算空格个数并打印出来
s=input("请输入字符串:")
count1=0
count2=0
for x in s:
    if x=="a":
        count1+=1
    if x==" ":
        count2+=1     
print("a的个数为：%d"%count1)
print("空格的个数为：%d"%count2)