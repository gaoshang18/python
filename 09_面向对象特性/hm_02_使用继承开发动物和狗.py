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

# 创建一个对象 -狗对象

wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

