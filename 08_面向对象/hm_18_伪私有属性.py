class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def secret(self):
        print("%s 的年龄是%d " % (self.name, self.__age))

xiaofang = Women("小芳")

# 私有属性 ，在外界不能够直接访问
# 可以用下划线_叫对象
print(xiaofang._Women__age)
# 私有方法同样也不能在外部调用
#  在属性和方法名前加 __ 两个下划线
xiaofang.secret()
