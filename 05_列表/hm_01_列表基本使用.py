name_list = ["zhangsan","lisi","wangwu"]

# 1.取值和索引
print(name_list[2])

# 知道数据内容，想确定数据在列表的位置
# 使用index方法需要注意，传递参数不在列表，程序会报错
print(name_list.index("lisi"))

# 2修改
name_list[1] = "李四"
# IndexError: list assignment index out of range
#
# name_list[3] = "wangwu"
# append在末尾添加
name_list.append("王小二")
# insert 在指定位置添加
name_list.insert(1,"小美眉")
# extend其它列表追加到当前列表
temp_list = ["孙悟空","猪八戒","沙悟净"]
name_list.extend(temp_list)
# 4.删除
# remove 从列表删除指定数据
name_list.remove("wangwu")
# pop默认删除列表最后元素
name_list.pop()
# pop默认删除列表指定位置的元素
name_list.pop(3)
print(name_list)
# clear 清空列表
name_list.clear()
print(name_list)
# 使用del关键字 delete删除列表元素
# del 关键字本质上是用来将一个变量从内存中删除的
# del 后后面的代码就不能使用这个变量了
name = "小明"
del name
print(name)
#del name_list[1]