import xlrd
import xlwt

def readexcel():
    # 这部分是读取内容

    workbook=xlrd.open_workbook(r'E:\用户新增表.xlsx')
    print(workbook.sheet_names())
    sheet2=workbook.sheet_by_name('用户新增表')
    nrows=sheet2.nrows #行数excl_1.0.py
    ncols=sheet2.ncols #列数
    print(nrows,ncols)


    cell_A=sheet2.cell(1,1).value #取第二行第二列内容
    print(cell_A)
    sheet = '用户新增表'
    EXcel = '用户新增表'
    row = nrows + 1
    col = 1
    s = '你好'
    print(row)
    #下面是写入内容 部门	账号	姓名	外包oa账号	岗位角色	创建时间	共享盘组
    sheet.write(row, col, s)
    EXcel.save('用户新增表.xlsx')
if __name__ == '__main__':
    readexcel()