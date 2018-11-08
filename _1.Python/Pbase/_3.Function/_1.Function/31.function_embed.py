# 31.function_embed.py
# 此示例示意函数嵌套定义:
def fn_outter():
    print("fn_outter被调用")
    def fn_inner():
        print("fn_inner被调用")
    fn_inner()
    fn_inner()
    print("fn_outter调用结束!")
fn_outter()
