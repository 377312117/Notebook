import re
import sys

def get_address(port):
    f = open('1.txt','r')
    # 通过port找到这一段
    # 首先对该段进行提取
    while True:
        data = ''
        for line in f:
            if line != '\n':   # 空行就是\n
                data += line
            else:
                break

        # 说明已经读到文件结尾
        if not data:
            return 'Not found the port'
            break
        # 匹配出首个单词
        try:
            PORT = re.match(r'\S+',data).group()  
            # match从开头匹配
        except Exception as e:
            print(e)
            continue

        if port == PORT:
            pattern = r'address is (\w{4}\.\w{4})'
            # ip 地址
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)'
            address = re.search(pattern,data).group()
            return address
        

if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))
# 难点:截取段,二次匹配,怎么用空行分组

# 首先进行定位,将每一段进行分组,利用正则表达式匹配关键字
# f = open('1.txt','r')
# while True:
#     data = f.readline()
#     if not data:
#         data = f.readline()
#         if not data:
#             break    
#     pattern = r'\b[A-Z]\S*(//[0-9])*'
#     l = re.search(pattern,data).group()
#     print(l)

# 匹配到正则表达式则进行定位,将继续匹配'Internet address is'
