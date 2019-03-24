# 计算 0~100之间所有数字的累计求和结果
# 1.定义一个整数的变量记录循环的次数
result = 0
i = 0
# 2.开始循环
while i <= 100:
    print(i)
    # 每次循环，都让result 这个变量和i这个计数器相加
    result += i
    # 处理计数器
    i += 1
    print("循环次数%d,共计为%d"%(i,result))