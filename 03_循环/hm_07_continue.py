i = 0
while i < 10:
    # continue 当某一条件满足时，不执行后续重复的代码
    # 在使用关键字之前需要确认循环的计数是否修改，否则可能会导致是循环
    if i == 3:
        print("over")
        i += 1
        continue
    print(i)
    i += 1