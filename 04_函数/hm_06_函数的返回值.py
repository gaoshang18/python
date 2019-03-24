# 函数的返回值 return


def sum_2_mun(num1,num2):
    """对两个数字的求和"""

    result = num1 + num2
    return  result
# return 接收返回值
# 可以使用变量,来接受函数执行的返回结果
sum_result = sum_2_mun(1,2)
print("计算求值结果%d" % sum_result)