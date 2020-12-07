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

    for i in range(1, col_num):
        if '结果' in sh.row_values(0)[i]:
            task_result_position = i

    for i in range(1, col_num):
        if '创建时间' in sh.row_values(0)[i]:
            task_create_time_position = i

    for i in range(1, col_num):
        if '上传时间' in sh.row_values(0)[i]:
            task_upload_time_position = i

    for i in range(1, col_num):
        if '失败信息' in sh.row_values(0)[i]:
            task_failure_message_position = i

    return data_list, task_result_position, task_create_time_position,task_upload_time_position,task_failure_message_position


def write_excel_xls(file_path, col, row, value):  # row行 col列
    """
    excel 写入
    :param row:
    :param col:
    :param value:
    :return:
    """
    book_r = xlrd.open_workbook(file_path)
    book_w = copy(book_r)  # 复制原表格
    sheet_1 = book_w.get_sheet(0)  # 以编辑方式得到文件的第一个工作表
    sheet_1.write(row, col, value)  # 把内容写入表格
    try:
        os.remove(file_path)  # 删除原文件
    except BaseException:
        print('ERROR:运行期间请关闭Excel文件，并重新运行程序！')
    book_w.save(file_path)  # 保存修改的文件为原文件