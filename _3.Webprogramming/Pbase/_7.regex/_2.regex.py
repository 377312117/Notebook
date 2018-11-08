import re

pattern = r'\d+'
s = '2008年事情多,08奥运,512地震'

it = re.finditer(pattern,s)

for i in it:
    # match对象group函数获取匹配内容
    print(i.group())

# 绝对匹配
try:
    obj = re.fullmatch(r"\w+",'hello1973')
    print(obj.group())
except AttributeError as e:
    print(e)

# 匹配开头位置
obj = re.match(r'[A-Z]\w+','Hello world')
print(obj.group())

# 匹配第一个符合条件的内容
obj = re.search(r'\d+',s)
print(obj.group())