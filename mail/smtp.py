# str= input("(是从excl复制的)例如\"chuan.li	李川\" input:")

str = 'chuan.li	李川'
txt = str.split("	", 1)
cdsid = txt[0]
user_name = txt[1]
user_passwd = cdsid.capitalize()

to_addr = "%s@anxincloud.com" %cdsid
print(11111)
print(to_addr)