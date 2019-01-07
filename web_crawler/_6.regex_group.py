import re 

s = 'A B C D'

p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

# 第一步,匹配整体正则['A B','C D']
# 第二步:匹配分组内容['A','C']
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))


# 第一步,匹配整体正则['A B','C D']
# 第二步:会把每一组作为元组作为元素存入列表,匹配分组内容[('A','B'),('C','D')]
p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))