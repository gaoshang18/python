from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = "shang.gao@anxincloud.com"
password = "JP5xzouV5bfsVSsF"
# to_addr = ['shang.gao@anxincloud.com']
smtp_server = "smtp.exmail.qq.com"

str= input("(是从excl复制的)例如\"chuan.li	李川\" input:")
# str = 'chuan.li	李川'
txt = str.split("	", 1)
cdsid = txt[0]
user_name = txt[1]
user_passwd = cdsid.capitalize()
to_addr = "%s@anxincloud.com" %cdsid
print(to_addr)
msg = MIMEText("""已为你开通以下账号
账号均为名.姓的拼音
姓名：	%s
1.计算机账号：		%s
密码：		%s123
修改密码		Ctrl+Alt+Delete
							
2.上网账号：		%s
密码：		123
认证地址
http://10.10.12.1
							
3.公共盘账号：		%s

密码： 		6
公共盘浏览路径  		计算机  \\192.168.20.101
							
修改密码地址
http://192.168.20.101/cgi-bin/changepassword.cgi
4.邮箱账号：		%s@anxincloud.com
密码：		%s123
邮箱登陆地址：	mail.anxincloud.com	或者https://exmail.qq.com/login 或者百度搜索“腾讯企业邮箱登陆”
5.oa地址	http://oa.anxincredit.com			密码默认为	1	账号:	工号(等录入人事系统后在告知)""" % (user_name, cdsid, user_passwd, cdsid, cdsid, cdsid, user_passwd),'plain', 'utf-8')
msg['From'] = _format_addr('高尚 <%s>' % from_addr)
msg['To'] = _format_addr('%s <%s>' % (user_name, to_addr))
msg['Subject'] = Header("账号密码告知", 'utf-8').encode()





server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
# 服务器返回值
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()