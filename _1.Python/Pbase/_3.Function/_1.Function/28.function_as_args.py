def f1():
    print("hello f1")
def f2():
    print("hello f2")
def fn(fn):
    print(fn)
    fn     # fn 指f1
fn(f1())

