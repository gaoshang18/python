# 1.判断空白字符 和其它空白字符
spce_str = "  \t\n\r"
print(spce_str)
print(spce_str.isspace())

# 2.判断字符串中只包含数字
# 1>都不能判断小数
# num_str = "1.1"
num_str = "①"
# num_str = "\u00b2"
print(num_str)
# 只能判断阿拉伯数字
print(num_str.isdecimal())
# 可判断特殊数字例如① \u00b2
print(num_str.isdigit())
# 可判断中文数字，① \u00b2
print(num_str.isnumeric())