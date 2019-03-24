# 函数的返回值 return
def print_line(char, times):


    print(char * times)


def print_lines(char, times,nul):
    """打印多行分割线

    :param char: 分割线使用的分割符
    :param times:分割线重复的次数
    :param nul:分割线打印的行数
    """
    row = 0
    while row < nul:
        print_line(char, times)
        row += 1

print_lines("hi",5,2)
