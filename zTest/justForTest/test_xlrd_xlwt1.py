import os
import xlrd
from xlutils.copy import copy

def write_excel_xls(row, col, value,data_file):
    """
    excel 写入
    :param row: 
    :param col: 
    :param value: 
    :return: 
    """
    book_r = xlrd.open_workbook(data_file)
    book_w = copy(book_r)  # 复制原表格
    sheet_1 = book_w.get_sheet(0)  # 以编辑方式得到文件的第一个工作表
    sheet_1.write(row, col, value)   # 把内容写入表格
    os.remove(data_file)  # 删除原文件
    book_w.save(data_file)  # 保存修改的文件为原文件

if __name__ == '__main__':
    data_file = 'I:\data.xlsx'
    write_excel_xls(5,6,'555',data_file)