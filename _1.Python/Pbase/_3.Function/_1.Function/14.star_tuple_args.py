#此示例示意星号元组形参的定义和使用
def func(*args):
    print("用户传入的参数个数是:",len(args))
    print("args=",args)
func()
#0,args=()
func(1,2,3)
#3,args=(1,2,3)
func(1,2,3,"AAA","BBB","CCC")