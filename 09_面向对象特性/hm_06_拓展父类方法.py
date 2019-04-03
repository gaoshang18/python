class Animal:

    def eat(self):
        print("吃___")

    def drink(self):
        print("喝___")

    def run(self):
        print("跑___")

    def sleep(self):
        print("睡___")


class Dog(Animal):

    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")
    #

    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):


    def fly(self):

        print("我会飞")

    def bark(self):

        # 1.针对子类特有的需求，编写代码

        print("神一样的叫唤。。。")
        # 2.使用 super().调用原本在父类中封装的方法
        # super().bark()

        # 使用父类名.方法（self）
        Dog.bark(self)
        # 注意： 如果使用子类调用犯法，会出现递归调用 - 是循环！！！！
        # XiaoTianQuan.bark(self)
        # 3.增加子类的方法
        print ("!@$@$#@%@%#@$#@$")
        # 早期方法  父类名，方法（self)

class Cat(Animal):

    def catch(self):
        print("抓耗子")

xtq = XiaoTianQuan()
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类重写的方法
xtq.bark()

#  xtq.ca 

