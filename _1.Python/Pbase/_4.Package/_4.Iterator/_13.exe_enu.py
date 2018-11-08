# 写一个程序,输入任意行文字,当输入空行时结束输入
# 打印带有行号的输入结果
def get_list():
    while True:
        s =input("请输入任意文字:")
        if s == "":   # if not s:
            break
        yield s
def main():
    L=list(get_list())
    # 用 enumerate 将L形成能提供的行号的可迭代对象
    for  t in enumerate(L,1):
        print("第 %d 行: %s" % t)
main()