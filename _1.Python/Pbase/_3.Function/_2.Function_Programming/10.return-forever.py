＃示意递归函数的用法
def say_story():
    print("从前有座山...")
    say_story()
    print("讲故事结束")
say_story()
print("讲故事结束")
