a = 6
b = 100
# 解法1： -使用变量

# c = a
# a = b
# b = c

# 解法2: -不使用其它变量
# a = a + b
# b = a - b
# a = a - b

# 解法3：-python专有解法，利用元组
# a,b = (b,a)
# 提示：等号右边的是一个元组，只是把小括号省略了
a,b = b,a
print(a)
print(b)