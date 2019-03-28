def demo1():
    num = 1
    print("在demo1函数内部的变量是 %d" % num)
    # 定义一个局部变量
    # 1> 出生：执行了num = 1
    # 2> 死亡：函数结束
def demo2():
    pass

    # print("%d " % num)
# 在函数位置定义的变量，不能在其他位置使用
# print("%d " % num)

demo1()
demo2()