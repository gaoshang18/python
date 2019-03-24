# 需求
# 1.定义布尔型变量 has_ticket 表示是否有车票
# 2.定义整型变量 knife_length 表示到的长度，单位：厘米
# 3.首先检查是否有车票，如果有，才允许进行 安检
# 4.安检时，需要检查刀的长度，判断是否超过 20 厘米
#
#     ·如果超过20厘米，提示刀的长度，不允许上车
#     ·如果不超过20厘米，安检通过
# 5.如果没有车票，不允许进门
has_ticket = False
knife_length = 20
if has_ticket:
    print("进行安检")
    if knife_length >= 20:
        print("刀的长度%d厘米大于等于20厘米，安检不通过。" %knife_length)
    else:
        print("安检通过")
else:
    print("没有车票，请先买票")  