import re

# s = 'Hello World'
# pattern = r'hello'

# regex = re.compile(pattern,flags=re.I)
# flags = re.I 不区分大小写

# s = '''hello world
# hello kitty
# 你好,北京
# '''

# pattern = r'.+'    #  .不能匹配换行
# regex = re.compile(pattern,re.S)
# # re.S 可以使.匹配换行

# s = '''hello world
# nihao beijing
# '''

# pattern = r"^nihao"
# regex = re.compile(pattern,re.M)


s = '''hello world
nihao beijing
'''

pattern = r'''hello    # 匹配hello
\s+      # 匹配空格
world     # 匹配world
'''
regex = re.compile(pattern,re.X)


try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)