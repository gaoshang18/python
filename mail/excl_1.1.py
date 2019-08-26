import xlrd
import xlwt
import xlutils
import datetime
from xlutils.copy import copy
# 导入copy模块


def readexcel():
    # 这部分是读取内容

    workbook=xlrd.open_workbook(r'E:\用户新增表.xlsx')
    print(workbook.sheet_names())
    # table = data.sheets()[0]  # 读取第一个（0）表单
    # print(table.nrows)  # 输出表格行数
    # print(table.ncols)  # 输出表格列数
    # print(table.row_values(0))  # 输出第一行
    # print(table.col_values(0))  # 输出第一列
    # print(table.cell(0, 2).value)  # 输出元素（0,2）的值
    sheet2 = workbook.sheet_by_name('用户新增表')
    nrows = sheet2.nrows  # 行数excl_1.0.py
    ncols = sheet2.ncols  # 列数
    print(nrows,ncols)
    depa = '网络营销部'  # 部门
    cdsid = 'zhanghao'  # 账号
    username = '谢明'   # 姓名
    oaid = 'w0021'  # oa
    gwjs = '岗位角色' # 岗位角色
    #tim = print(time.strftime('%Y%m%d',time.localtime(time.time())))

    pub = 'oc'
    wb = copy(workbook)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)


    style = xlwt.XFStyle()
    style.num_format_str = 'M/D/YY'  # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
    #worksheet.write(0, 0, datetime.datetime.now(), style)

    ws.write(nrows, 0, label=depa)
    ws.write(nrows, 1, label=cdsid)
    ws.write(nrows, 2, label=username)
    ws.write(nrows, 3, label=oaid)
    ws.write(nrows, 4, label=gwjs)
    ws.write(nrows, 5, datetime.datetime.now(), style)
    ws.write(nrows, 6, label=pub)

    wb.save('E:\用户新增表.xlsx')  # 保存文件


if __name__ == '__main__':
    readexcel()