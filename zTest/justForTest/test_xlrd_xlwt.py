import os
import xlrd
from xlutils.copy import copy

# def base_dir(filename=None):
#     return os.path.join(os.path.dirname(__file__),filename)

"""对excel进行操作"""
work = xlrd.open_workbook('I:\data.xls')
# 索引到第X个工作表
sheet = work.sheet_by_index(0)
# 查看有多少行
print(sheet.nrows)
# 查看有多少列
print(sheet.ncols)
# 获取单元格内容
print(sheet.cell_value(1, 2))

"""对excel进行修改/添加内容"""

# 找到需要更该的xls
work = xlrd.open_workbook('I:\data.xls')
print(work)
# 对数据表格进行复制
old_content = copy(work)
# 定位到Sheet1表
ws = old_content.get_sheet(0)
# 在sheet1表中写入内容
ws.write(7, 2, "Tao")
# 对修改后的内容进行保存
old_content.save('I:\data1.xls')
