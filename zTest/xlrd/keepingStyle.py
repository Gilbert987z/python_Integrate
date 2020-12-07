# coding = utf-8

import requests
import json
import os
import xlrd
from xlutils.copy import copy
import xlwt
import time
import sys
from datetime import datetime




def get_excel_data(file_path, sheet_name):
    '''
    读取Excel
    '''
    bk = xlrd.open_workbook(file_path)  # 打开Excel文档
    sh = bk.sheet_by_name(sheet_name)  # 打开sheet
    row_num = sh.nrows  # 行数 11=10+1
    col_num = sh.ncols  # 列数
    data_list = []  # 列表

    for i in range(1, row_num):  # 循环行数 从第2行开始，到11行结束
        row_data = sh.row_values(i)  # 行 ['X70TESTVIN0000038', 'YODOTEST_20200801_#38_30']
        data = {}
        for index, key in enumerate(sh.row_values(0)):  # 枚举，创建出键值对 第一行 ['VIN', '任务名称']
            data[key] = row_data[index]

        data_list.append(data)

    return data_list


def write_excel_xls(file_path, col, row, value):  # row行 col列
    """
    excel 写入
    :param row:
    :param col:
    :param value:
    :return:
    """
    book_r = xlrd.open_workbook(file_path,formatting_info=True)
    book_w = copy(book_r)  # 复制原表格
    sheet_1 = book_w.get_sheet(0)  # 以编辑方式得到文件的第一个工作表


    sheet_1.write(row, col, value,set_style('宋体',400,'0x0C',bold=True))  # 把内容写入表格
    try:
        os.remove(file_path)  # 删除原文件
    except BaseException:
        print('ERROR:运行期间请关闭Excel文件，并重新运行程序！')
    book_w.save(file_path)  # 保存修改的文件为原文件

def set_style(name, height,color, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.name = name
    # 是否为粗体
    font.bold = bold
    # 设置字体颜色
    font.colour_index = color
    # 字体大小
    font.height = height
    # 字体是否斜体
    font.italic = True
    # 字体下划,当值为11时。填充颜色就是蓝色
    font.underline = 0
    # 字体中是否有横线struck_out
    font.struck_out =True
    # 定义格式
    style.font = font

    return style


file_path = r'C:\Users\天籁纸鸢\Desktop\test.xlsx'
sheet_name = 'Sheet1'
# print(get_excel_data(file_path, sheet_name))

# write_excel_xls(file_path, 5, 5,
#                 'task_result_status')  # 写入升级结果的数据  excel_data[1]是返回的第二个数据
# write_excel_xls(file_path, 5, 6,
#                 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 写入升级时间





font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 4
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 'Test', style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

wb.save(r'C:\Users\天籁纸鸢\Desktop\test.xlsx')