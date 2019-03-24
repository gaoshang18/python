num_str = "0123456789"
# 1.截取 2~5 位置的字符串
print(num_str[2:6])
# 2.截取 2~ 末尾的字符串
print(num_str[2:])
# 3.截取 开始~5 位置的字符串
print(num_str[:6])
# 4.截取 完整的字符串
print(num_str[:])
# 5.从开始位置每隔一个字符截取字符串
print(num_str[0::2])
# 6.从索引1开始2，每隔一个一个取
print(num_str[1::2])
# 7.截取 2~末尾 -1 的字符串
print(num_str[2:-1])
# 8.截取字符串末尾两个字符
print(num_str[-2:])
# 9.字符串的逆序（面试题）
print(num_str[::-1])