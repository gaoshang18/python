# 假设：以下内容是从网络上抓取的
# 要求: 顺序并且居中对齐输出以下内容

poem_str = "登鹳雀楼\t 王焕之\t 白日依山尽\t 黄河入海流\t \n 欲穷千里目 \t\t更上一层楼"
print(poem_str)
# 1.拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 2.合并字符串
result = "\n".join(poem_list)
print(result)
