import re

pattern = r'\w + \d+'
s = 'zhang:1994'

# re直接调用
l = re.findall(pattern,s)
print(l)

# regex调用
regex = re.compile(pattern,flags=0)
l = regex.findall(s,pos=0,endpos=12)
print(l)

# 对字符串进行分割,分割符为任意1个或多个空格
l1 = re.split(r'\s+','Hello world')
print(l1)
# 返回['Hello', 'world']

s = re.sub(r'\s+','##','hello world',5)
print(s)
# 默认全部替换,如果最大替换值不足以全部替换,则从前面开始替换
# 返回  hello##world