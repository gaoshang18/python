# 注意：在开发时，应该把模块中的所有全局变量全局变量
# 定义在所有函数的上方，就可以保证所有的函数
# 都能正常的访问到每一个全局变量
num = 10
gl_title = "黑马程序员"
name = "小明"


def demo():
    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    # print("%s" % name)

# 在定义一个全局变量


demo()

# 在定义一个全局变量
