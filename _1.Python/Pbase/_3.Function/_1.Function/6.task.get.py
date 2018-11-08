#写一个函数get_chinese_char_count(s)函数,
# 此函数实现的功能是给定一个字符串,返回这个字符串中文文字字符的个数
# def get_chinese_char_count(s):
#     ...    #此处自己实现
# s=input("请输入中英文混合的字符串:")
# print("您输入的中英文字符的个数是:"
#     get_chinese_char_count(s))
def get_chinese_char_count(x):
    count=0
    #此处用来计数
    for ch in s:
        #如果涉及到中英文字符的比较或者筛选,
        # 调出字符函数把两者进行处理用同一种筛选方法
        if ord(ch)>127:
            count+=1
    return count
s=input("请输入字符串:")
length=get_chinese_char_count(s)
print("您输入的中文字符的个数是:",length)