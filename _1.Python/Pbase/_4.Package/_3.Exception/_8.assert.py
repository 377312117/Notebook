#此示例示意assert语句的用法:
def get_score():
    s = int(input("请输入学生成绩(0~100):"))
    assert 0 <= s <= 100,"成绩超出范围"
    # 等同于 if bool(0 <= s <= 100) == False:
    #             raise AssertionError("成绩超出范围")
    return s
try:
    score = get_score()
    print("学生成绩为:", score)
except AssertionError:
    print("用户输入的成绩超出范围")
