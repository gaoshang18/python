# -*- coding: UTF-8 -*-

from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict, load_single_dict
from pypinyin.style import register


def piny(name1):
    sid = lazy_pinyin(name1)
    print(sid)
    return sid

def cds(name):

    cdsid1 = name[:-1]
    user_name = name[-1]
    cdsid1.insert(0, '.')
    cdsid1.insert(0, user_name)
    txt = "".join(cdsid1)
    return txt


ttt = input("请输入姓名:")
pyname = piny(ttt)
cdsid = cds(pyname)

