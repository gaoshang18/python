# 定义字符串变量 name,输出 我的名字叫 小明，请多多关照！
name = "ttt明"

print("我的名字叫 %s，请多多关照！" %name)
# 定义一个整数变量 student_no,输出 我的学号是000001
student_no = 158
print("我的学号是%06d" % student_no)
# 定义小数price、weight、money，输出 苹果的单价是9.00元/斤，购买5.00斤，需要45.00元
price = 8.5 ; weight = 5.2 ; money = price * weight
print("苹果的单价是%.02f元/斤，购买%.02f斤，需要%.02f元" %(price, weight ,money))
# 定义一个小数scale,输出 数据比例是10.00%
scale = 0.8
print("数据比例是%.02f%%" % (scale * 100))