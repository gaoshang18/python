# 在控制台连续输入五行*，每行星号的数量依次增加
#方法一
# print("方法一")
row = 1
while row <= 9:
    col = 1
    while col <= 9:
        nob = row * col
        if col > row:
            col += 1
            continue
        print("%d*%d=%d"%(col,row,nob),end=" ")
        col += 1
    print("")
    row += 1
# 方法二
print("方法二")
row = 1
while row <= 9:
    col = 1
    while col <= row:
        #print("*",end="")
        print("%d * %d = %d" % (col,row,col * row), end="\t")

        col += 1
    print("")
    row += 1
print("1\t2\t3") # \t 在控制台输出一个 制表符 ，协助在输出文本时 垂直方向 保持对齐
print("10\t20\t30")

# \n 在控制台输出一个 换行符  \"可以在控制台输出"
print("Hello\nPython")