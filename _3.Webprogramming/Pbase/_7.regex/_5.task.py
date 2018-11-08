import re 

f = open('text.txt','rb')
data = f.read()

pattern = r'\b[A-Z]\S*'
# 大写字母开头的单词
l = re.findall(pattern,data)

print(l)

pattern = r'-?\d+\.?/?\d*%?'
# 匹配整数,小数,百分数,负数,分数
l = re.findall(pattern,data)
print(l)