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
        print("%d * %d = %d" % (col,row,col * row), end=" ")

        col += 1
    print("")
    row += 1