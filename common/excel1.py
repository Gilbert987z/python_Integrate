# coding = utf-8

import os
import xlrd
from xlutils.copy import copy


#
# 数据模块
#



def get_excel_data(file_path, sheet_name):
    '''
    读取Excel
    '''

    book = xlrd.open_workbook(file_path)  # 打开Excel文档
    sheet = book.sheet_by_name(sheet_name)  # 打开sheet

    row_num = sheet.nrows  # 行数 11=10+1   获取某sheet中的有效行数
    col_num = sheet.ncols  # 列数  获取某sheet中的有效列数

    first_row_list = sheet.row_values(0)  #第一行的数据列表

    data_list = []  # 键值对的数据列表

    for i in range(1, row_num):  # 循环行数 从第2行开始，到11行结束
        row_data = sheet.row_values(i)  # 行 ['X70TESTVIN0000038', 'YODOTEST_20200801_#38_30']
        data = {}

        for index, key in enumerate(sheet.row_values(0)):  # 枚举，创建出键值对 第一行 ['VIN', '任务名称']
            data[key] = row_data[index]

        data_list.append(data)

    return data_list, first_row_list




def write_excel_xls(file_path, sheet_name, row, col, value):  # row行 col列
    """
    excel 写入
    :param row:
    :param col:
    :param value:
    :return:
    """
    book_r = xlrd.open_workbook(file_path)  # 保留样式

    sheet_names = book_r.sheet_names()  #读取sheet的所有数据，列表
    sheet_index = sheet_names.index(sheet_name) #获取sheet_name所在的位置，index

    book_w = copy(book_r)  # 复制原表格
    sheet = book_w.get_sheet(sheet_index)  # 以编辑方式得到文件的指定列表工作表
    sheet.write(row, col, value)  # 把内容写入表格
    try:
        os.remove(file_path)  # 删除原文件
    except Exception as e:
        print('ERROR:运行期间请关闭Excel文件，并重新运行程序！')
    book_w.save(file_path)  # 保存修改的文件为原文件





