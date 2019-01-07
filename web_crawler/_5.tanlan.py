import re

html = """
    <div><p>苟利国家生死以</p></div>
    <div><p>岂因祸福避趋之</p></div>
"""


# 创建编译对象,贪婪匹配
p = re.compile('<div><p>.*</p></div>',re.S)
r = p.findall(html)
print(r)
# ['<div><p>苟利国家生死以</p></div>\n    <div><p>岂因祸福避趋之</p></div>']

# 创建编译对象,非贪婪匹配
p = re.compile('<div><p>.*?</p></div>',re.S)
r = p.findall(html)
print(r)
# ['<div><p>苟利国家生死以</p></div>', '<div><p>岂因祸福避趋之</p></div>']