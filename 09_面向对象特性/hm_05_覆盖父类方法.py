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

        print("叫得和神一样。。。")


class Cat(Animal):

    def catch(self):
        print("抓耗子")
# 创建一个对象 -哮天犬狗对象
xtq = XiaoTianQuan()
# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法时，会调用子类重写的方法
xtq.bark()

#  xtq.ca 

