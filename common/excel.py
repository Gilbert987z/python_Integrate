# coding = utf-8

import os
import xlrd
import xlwt
import time
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
        if '升级指令发送时间' in sh.row_values(0)[i]:
            task_create_time_position = i

    for i in range(1, col_num):
        if '最后一次报文时间' in sh.row_values(0)[i]:
            task_upload_time_position = i

    for i in range(1, col_num):
        if '失败信息' in sh.row_values(0)[i]:
            task_failure_message_position = i

    return data_list, task_result_position, task_create_time_position, task_upload_time_position, task_failure_message_position


def write_excel_xls(file_path, row, col, value):  # row行 col列
    """
    excel 写入
    :param row:
    :param col:
    :param value:
    :return:
    """
    book_r = xlrd.open_workbook(file_path)  # 保留样式
    book_w = copy(book_r)  # 复制原表格
    sheet_1 = book_w.get_sheet(0)  # 以编辑方式得到文件的第一个工作表
    sheet_1.write(row, col, value)  # 把内容写入表格
    try:
        os.remove(file_path)  # 删除原文件
    except BaseException:
        print('ERROR:运行期间请关闭Excel文件，并重新运行程序！')
    book_w.save(file_path)  # 保存修改的文件为原文件


def creat_excel(file_path):
    # workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
    # sheet1 = workbook.add_sheet("测试表格")  # 新建sheet
    # workbook.save(r'D:\PycharmProjects\test.xlsx')  # 保存

    # 创建excel文件
    filename = xlwt.Workbook(encoding='utf-8')
    # 给工作表命名，test
    sheet = filename.add_sheet('测速信息')
    

    # # 写入内容，第4行第3列写入‘张三丰’
    # hello=u'张三丰'
    # sheet.write(3,2,hello)

    # 默认写入第一行的信息
    sheet.write(0, 0, '编号')
    sheet.write(0, 1, '测速时间')
    sheet.write(0, 2, 'Ping/ms')
    sheet.write(0, 3, '下载/Mbps')
    sheet.write(0, 4, '上传/Mbps')
    sheet.write(0, 5, '运营商')
    sheet.write(0, 6, '城市')
    sheet.write(0, 7, '测速节点')


    create_excel_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    file_path = file_path + r'\测速结果' + create_excel_time + '.xlsx'
    # 指定存储路径，如果当前路径存在同名文件，会覆盖掉同名文件
    filename.save(file_path)

    return file_path, sheet