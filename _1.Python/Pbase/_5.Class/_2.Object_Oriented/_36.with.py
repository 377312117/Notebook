# 此函数示意with的用法
try:
    with open("text.txt"."w") as f:
        s = int(input("请输入整数"))    # 故意制造异常
        f.write("hello")
except OSError:
    print("文件打开失败")
except:
    print("读取文件失败 ")