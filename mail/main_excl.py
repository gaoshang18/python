# -*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from pypinyin import lazy_pinyin
import xlrd
import xlwt
import xlutils
import datetime
from xlutils.copy import copy


def piny(name1):
    """

    :param name1:
    :return: 拼音
    """
    sid = lazy_pinyin(name1)
    return sid


def cds(name):
    """

    :param name:
    :return: 用户id
    """
    cdsid1 = name[:-1]
    user_name = name[-1]
    cdsid1.insert(0, '.')
    cdsid1.insert(0, user_name)
    txt = "".join(cdsid1)
    return txt


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def mail(user_name,cdsid):
    """
    邮件发送
    """
    from_addr = "shang.gao@anxincloud.com"
    password = "JP5xzouV5bfsVSsF"
    # to_addr = ['shang.gao@anxincloud.com']
    smtp_server = "smtp.exmail.qq.com"

    user_passwd = cdsid.capitalize()
    to_addr = "%s@anxincloud.com" % cdsid
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
    5.oa地址	http://oa.anxincredit.com			密码默认为	1	账号:	工号(等录入人事系统后在告知)""" % (
    user_name, cdsid, user_passwd, cdsid, cdsid, cdsid, user_passwd), 'plain', 'utf-8')
    msg['From'] = _format_addr('高尚 <%s>' % from_addr)
    msg['To'] = _format_addr('%s <%s>' % (user_name, to_addr))
    msg['Subject'] = Header("账号密码告知", 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def readexcel(depa, cdsid, username, oaid, gwjs, pub):
    """

    :param depa: 部门
    :param cdsid: id
    :param username:用户名
    :param oaid:
    :param gwjs:
    :param pub:
    """
    workbook=xlrd.open_workbook(r'E:\用户新增表.xlsx')
    # print(workbook.sheet_names())
    sheet2 = workbook.sheet_by_name('用户新增表')
    nrows = sheet2.nrows  # 行数excl_1.0.py
    ncols = sheet2.ncols  # 列数

    wb = copy(workbook)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)


    style = xlwt.XFStyle()
    style.num_format_str = 'M/D/YY'
    ws.write(nrows, 0, label=depa)
    ws.write(nrows, 1, label=cdsid)
    ws.write(nrows, 2, label=username)
    ws.write(nrows, 3, label=oaid)
    ws.write(nrows, 4, label=gwjs)
    ws.write(nrows, 5, datetime.datetime.now(), style)
    ws.write(nrows, 6, label=pub)

    wb.save('E:\用户新增表.xlsx')  # 保存文件
    print("%sexcl写入成功" % username)

if __name__ == '__main__':
    name = input("请输入姓名:")
    depa = input("请输入部门:")
    oaid = input("请输入oaid:")
    gwjs = input("请输入岗位角色id:")
    pub = input("请输入共享组:")
    pyname = piny(name)
    cdsid = cds(pyname)
    mail(name,cdsid)
    readexcel(depa, cdsid, name, oaid, gwjs, pub)
