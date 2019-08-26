# -*- coding: UTF-8 -*-

from pypinyin import lazy_pinyin

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


name = input("请输入姓名:")
pyname = piny(name)
cdsid = cds(pyname)
print(name)
print(cdsid)
