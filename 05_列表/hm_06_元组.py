name_list = ("张三",18,1.75,)
print(type(name_list))
# 定义一个只包含一个元素的元组
single_tuple = (5)
print(type(single_tuple))
single_tuple2 = (5,)
print(type(single_tuple2))

# 1.取值和取索引
print(name_list[0])
# 已经知道数据的内容，希望知道该数据在元组中的索引
print(name_list.index("张三"))
# 2.统计计数
print(name_list.count("张三"))
# 统计元组中包含元素的个数
print(len(name_list))