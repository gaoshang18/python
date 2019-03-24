name_list = ["zhangsan","lisi","wangwu","zhangsan"]

# len(length 长度) 函数可以统计列表中元素的总数
list_len =len(name_list)

print("列表中包含 %d 个元素"% list_len)
# count 方法可以统计列表中某一数据出现的次数
count = name_list.count("zhangsan")
print("列表中zhansan出现了 %d 次"% count)
# 从列表中删除数据 第一次的数据如果不存在将报错
name_list.remove("zhangsan")
print(name_list)