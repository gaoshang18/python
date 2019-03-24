# 注意函数定义完成后，只表示函数封装了这一段代码而已
# 如果不主动调用函数，函数封装的代码不会执行
name = "小明"


def say_hello():
    """打招呼"""

    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)


say_hello()


print(name)