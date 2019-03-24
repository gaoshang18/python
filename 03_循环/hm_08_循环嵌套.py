# 在控制台连续输入五行*，每行星号的数量依次增加
#方法一
# print("方法一")
row = 1
while row <= 5:
    print("*" * row )
    row += 1
# #方法二
# print("方法二")
row1 = 1
row2 = 1
while row1 <= 5:
    # 在默认情况下，print 函数输出内容之后，会自动在内容末尾添加换行
    # 可以 print("*", end="") end=""后不换行
    # while row1 :
    #  print("*",end="")
    col = 1
    # 开始循环
    """
    1 1次=row
    12 2次=row
    123 3次=row
    1234 4次=row
    12345 5次=row
    """
    while col <= row1:
        print("*", end="")
        col += 1
    print("")
    # 打印换行
    row1 +=1
