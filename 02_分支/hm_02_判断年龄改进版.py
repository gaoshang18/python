# 输入用户年龄
# age = 15
# age = input("请输入年龄")
age = int(input("请输入年龄"))
# 判断是否满足 18 岁
if age >= 18:

    # 若果满足 18 岁，允许进入网吧嗨皮
    print("你已经成年，欢迎进入网吧嗨皮")
else:
    # 若果未满 18 岁，提醒回家写作业
    print("你还没有成年，请回家做作业吧")
# 这句代码什么时候都会执行！
print("这句代码什么时候执行")