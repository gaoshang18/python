# 假设：以下内容是从网络上抓取的
# 要求: 顺序并且居中对齐输出以下内容

poem = ["\t\n登鹳雀楼",
        "王焕之",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"]
for poem_str0 in  poem:
    print("|%s|" % poem_str0.strip().center(10,"　"))

for poem_str in poem:
    #　　中文输入法全半角输入
    print("|%s|"% poem_str.center(10, "　"))
for poem_str1 in poem:
    print("|%s|" % poem_str1.ljust(10, "　"))

