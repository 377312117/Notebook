import re

pattern = r'(ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

# 获取match对象
# obj = regex.search('abcdef')
obj = regex.search('abcdefgh',pos=0,endpos=6)

# obj属性变量
print(obj.pos)
# --> 0 目标子串的起始位置
print(obj.endpos)
# --> 8 目标子串的末尾位置
print(obj.re)
# --> re.compile('abcdef')    正则表达式
print(obj.string)
# --> abcdefgh                目标字符串
print(obj.lastgroup)           # 最后一组的组名
print(obj.lastindex)           # 最后一组是第几组


print(obj.span())     # 匹配内容的起止位置
print(obj.start())    # 匹配内容的起始位置
print(obj.end())      # 匹配位置的终止位置

print(obj.group())
print(obj.group(1))
print(obj.group('dog'))

print(obj.groupdict())
print(obj.groups())
