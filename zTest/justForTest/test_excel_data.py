import xlrd


def get_excel_data(file_path, sheet_name):
    '''
    读取Excel
    '''
    bk = xlrd.open_workbook(file_path)  # 打开Excel文档
    sh = bk.sheet_by_name(sheet_name)  # 打开sheet
    row_num = sh.nrows  # 行数 11=10+1\
    col_num = sh.ncols  #列数
    data_list = []  # 列表

    for i in range(1, row_num):  # 循环行数 从第2行开始，到11行结束
        row_data = sh.row_values(i)  # 行 ['X70TESTVIN0000038', 'YODOTEST_20200801_#38_30']
        # print(row_data)
        data = {}
        for index, key in enumerate(sh.row_values(0)):  # 枚举，创建出键值对 第一行 ['VIN', '任务名称']
            data[key] = row_data[index]

        data_list.append(data)

    print(col_num)
    print(sh.row_values(0))
    for i in range(1, col_num):
        print(sh.row_values(0)[i])
        if '升级结果' == sh.row_values(0)[i]:
            task_result_position = i
            print(i)

    return data_list,task_result_position

excel_data = get_excel_data('I:\data.xlsx','Sheet1')
print(excel_data)
print(excel_data[0])
print(excel_data[1])
