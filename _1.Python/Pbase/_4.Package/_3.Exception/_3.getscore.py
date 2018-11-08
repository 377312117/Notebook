#输入学生成绩,不是0~100返回0,否则返回输入的整数
def get_score():
    score=int(input("请输入学生成绩(0~100):"))
    if 0<=score<=100:
        print("学生成绩是:",c)
    else:
        print("学生成绩是:",0)
try:
    score=get_score()
except ValueError:
    score=0
print("您的成绩是;",score)

#在函数内部加入try语句进行错误处理
def get_score():
    try:
        score=int(input("请输入学生成绩(0~100):"))
    except ValueError:
        return 0
    if not (0<=s<=100):
        return 0
    return s